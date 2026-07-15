

## Lab : Déploiement d’un Cluster Amazon EKS avec une Application Web

Objectif
- Créer un cluster Amazon EKS avec des nœuds managés.
- Déployer une application Nginx sur le cluster.
- Exposer l’application via un Load Balancer.
- Mettre en place l’autoscaling des pods.
- Gérer l’accès réseau avec des Security Groups et IAM Roles.

## packages
choco install -y eksctl
choco upgrade -y eksctl
eksctl version


eksctl create cluster --name $CLUSTER_NAME --region $REGION --nodegroup-name $NODEGROUP_NAME --node-type t3.medium --nodes 2 --nodes-min 2 --nodes-max 4 --managed


Loadbalncer: 10.100.226.117 


install helm
windows
linux

Add the stable repository to your local Helm installation on Windows