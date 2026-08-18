import io
import os
import urllib.parse
import boto3
from PIL import Image

s3_client = boto3.client('s3')

# Taille maximale de la miniature (largeur, hauteur en pixels)
THUMBNAIL_SIZE = (128, 128)

def lambda_handler(event, context):
    # 1. Récupération des informations sur l'événement S3
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        # Décodage du nom de fichier au cas où il contient des espaces ou caractères spéciaux
        image_key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
        
        # Éviter une boucle infinie si une miniature est traitée par erreur
        if image_key.startswith("thumb-"):
            continue

        try:
            # 2. Téléchargement de l'image depuis le bucket source
            response = s3_client.get_object(Bucket=source_bucket, Key=image_key)
            image_content = response['Body'].read()

            # 3. Traitement de l'image avec Pillow
            with Image.open(io.BytesIO(image_content)) as image:
                # Conservation du mode RVB pour le format JPEG
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                
                # Redimensionnement tout en conservant le ratio d'aspect
                image.thumbnail(THUMBNAIL_SIZE)

                # Sauvegarde de l'image modifiée dans un buffer en mémoire
                buffer = io.BytesIO()
                image.save(buffer, format="JPEG")
                buffer.seek(0)

            # 4. Définition du nom du fichier miniature
            file_name = os.path.basename(image_key)
            thumbnail_key = f"thumb-{file_name}"

            # 5. Envoi du thumbnail vers le bucket de destination
            # ATTENTION : Remplacez <prenom> par votre vrai prénom comme indiqué à l'étape 2 du TP !
            s3_client.put_object(
                Bucket="simon-thumbnails-bucket", 
                Key=thumbnail_key, 
                Body=buffer, 
                ContentType="image/jpeg"
            )

            print(f"Thumbnail créé avec succès : {thumbnail_key}")

        except Exception as e:
            print(f"Erreur lors du traitement de {image_key} dans {source_bucket}: {e}")
            raise e