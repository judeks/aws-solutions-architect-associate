# Explorer et utilisation EC2 Instance Metadata

* Lancer une instance EC2 sous AWS

* Comprendre et utiliser Instance Metadata Service(IMDS)

* Recuperer les metadata de l'instance depuis le terminal

* Experimenter IMDSv2 pour une meilleure securite.



# access metadata V1 LESS secure

    # application qui a besoin d'afficher ou qui a besoin des donnees de l'instance(VM)

    1- curl http://169.254.169.254/latest/meta-data/

       Exemple sortie:

        ami-id
        instance-id
        instance-type
        local-ipv4
        public-ipv4
        security-groups

# access metada V2 withe more secure

     2- TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

       exemple: 

          tous les metadata

          curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/


         recuperer l'ID de l'instance avec IMDSv2
         
               curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id


     3 - Forcer l'access aux metadata en exigeant le token sur l'instance


            - acceder a cloudshell
            - aws ec2 modify-instance-metadata-options --instance-id i-xxxxxxxxxx --http-tokens required(xxxxxxxxxx --> instance-id)
            
     4- Automatisation avec script shell

