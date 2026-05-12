
# Lab VPC Peering

  * Explorer le template CloudFormation en creant une pile
  * Creer 2 VPC avec 2 EC2 avec AWS CloudFormation
  * Mettre en place le VPC peering entre VPC1 et VPC2
  * Mettre a jour les tables de routage(Subnet 1 et Subnet2)
  * Se connecter ensuite a EC2 dans VPC1
  * Tester la connectivite vers EC2 dans VPC2
  * Nettoyer les ressources

  # Architecture AWS: VPC peering

  ![VPC peering](images/vpc-peering.png)

   * Mise en place connexion VPC peering

   ![VPC peering](images/vpc-peering-connection.png)

   * Routage vers VPC1 en etant dans subnet-2

   ![VPC peering](images/4-route-vers-vpc1.png)

   * Routage vers VPC2 en etant dans le subnet-1

   ![VPC peering](images/3-route-vers-vpc2.png)

