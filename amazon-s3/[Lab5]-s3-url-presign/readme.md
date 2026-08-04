Architecture

✅ Créer un bucket S3 privé.
✅ Envoyer un fichier dans le bucket.
✅ Générer une URL pré-signée avec AWS CLI et Python (Boto3).
✅ Tester l’accès au fichier via l’URL générée.


## Create bucket
- aws s3api create-bucket --my-bucket-simon-presigned-123 --region us-east-1 --create-bucket-configuration LocationConstraint=us-east-1

## l’upload 
- aws s3 cp private-test.txt s3://my-bucket-simon-presigned-123/

## Générer une URL Pré-signée avec AWS CL valable 2 minutes (120 secondes)

- aws s3 presign s3://my-bucket-simon-presigned-123/private-test.txt --expires-in 120

## Resultat

https://my-bucket-simon-presigned-123.s3.amazonaws.com/private-test.txt?AWSAccessKeyId=AKIAXBMDOEXIRULIV44R&Signature=RsGmCgg4GPxoicysLbTqED7R7K8%3D&Expires=1785334123


## Générer une URL Pré-signée avec Python (Boto3)

   - pip install boto3
   - Script Python pour générer une URL pré-signée
      ------------------------------------
        import boto3
        # Configurer le client S3
        s3_client = boto3.client("s3")
        # Paramètres
        bucket_name = "mon-bucket-presigned-url"
        object_name = "fichier-prive.txt"
        expiration = 600  # 10 minutes
        # Génération de l'URL pré-signée
        url_presignee = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_name},
            ExpiresIn=expiration,
        )
        print("URL Pré-signée :", url_presignee)

##  Nettoyage des Ressources

- aws s3 rm s3://my-bucket-simon-presigned-123/private-test.txt
- aws s3 rb s3://my-bucket-simon-presigned-123 --force


## Conclusion
✔️ Nous avons appris à générer et utiliser des URL pré-signées pour un accès temporaire sécurisé aux objets S3.
✔️ Nous avons utilisé AWS CLI et Boto3 (Python) pour automatiser ce processus.
✔️ Nous avons testé l’expiration automatique de l’URL.