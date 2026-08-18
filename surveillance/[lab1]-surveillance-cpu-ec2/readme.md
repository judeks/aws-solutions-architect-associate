

## Instructions

* Lancer une instance EC2 sous AWS
* Creer une alarme CloudWatch et un topic SNS
* Generer de la charge CPU
* Verifier que l'alarm passe au staut ALARM et qu'une notification SNS est envoyee

command

* sudo um install -y stress
* stress --cpu 2 --timeout 300