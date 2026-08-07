# Automatisation du tagging avec AWS S3 Batch

1. Génération de fichiers

2. Téléversement des fichiers vers S3

Transférez ces fichiers dans le bucket S3 :
aws s3 sync . s3://s3-batch-simon-lab/ --exclude "*" --include "file*"

3. Vérification du téléversement
Listez les fichiers dans le bucket pour confirmer leur présence :

aws s3 ls s3://s3-batch-simon-lab/
