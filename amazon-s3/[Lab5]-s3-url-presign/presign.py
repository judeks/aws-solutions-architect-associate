import boto3
# Configurer le client S3
s3_client = boto3.client("s3")
# Paramètres
bucket_name = "my-bucket-simon-presigned-123"
object_name = "private-test.txt"
expiration = 600  # 10 minutes
# Génération de l'URL pré-signée
url_presignee = s3_client.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket_name, "Key": object_name},
    ExpiresIn=expiration,
)
print("URL Pré-signée :", url_presignee)