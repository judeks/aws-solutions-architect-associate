
1. Architecture du Lab
L’architecture repose sur AWS Step Functions pour orchestrer l’exécution de plusieurs fonctions Lambda :

Une première fonction Lambda reçoit une entrée utilisateur.
Une deuxième fonction Lambda effectue un traitement.
Une troisième fonction Lambda enregistre le résultat final.

## Instructions

Créer un workflow Step Functions.
Définir plusieurs étapes (states) exécutant des fonctions Lambda.
Configurer les permissions nécessaires.
Tester le workflow et observer son exécution