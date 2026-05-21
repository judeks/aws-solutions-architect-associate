
# Mise en place d'une architecture Network LoadBalancer AWS

 * Creer deux instances EC2 qui affiche leur identifiant sur une page web
 * Creer un group de securote pour NLB qui accepte le port 80 HTTP
 * Creer un groupe cible
     - En production creer un autoscaling group qui lance les instances ec2 qui va les repartir sur differents zones de disponiblites
 * Creer un NLB (Network LoadBalancer) pour une tres haute performance

 * Acceder aux instances via NLB par le nom DNS
 * Nettoyer les ressources