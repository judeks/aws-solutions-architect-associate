
## Gestion du Cycle de Vie des Objets S3 avec S3 Lifecycle Policies

aws s3api create-bucket --bucket simon-lab-s3-lifecycle --region us-east-1 --create-bucket-configuration LocationConstraint=us-east-1

echo "Ceci est un fichier de test" > test-file.txt


aws s3 cp test-file.txt s3://simon-lab-s3-lifecycle/


aws s3api head-object --bucket simon-lab-s3-lifecycle --key test-file.txt --query "StorageClass"



✔️ Nous avons appris à créer une règle de cycle de vie S3 pour gérer le stockage automatiquement.
✔️ Nous avons configuré une transition entre différentes classes de stockage et une expiration des objets.
✔️ Nous avons exploré comment tester et vérifier la politique appliquée.
