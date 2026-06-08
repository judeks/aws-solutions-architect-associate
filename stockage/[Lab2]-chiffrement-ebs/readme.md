Lancer une instance EC2 avec 2 volumes EBS :

 1 volume Racine chiffré et 1 volume additionnel non chiffré

Montrer pour le volume EBS non chiffré

1 snapshot sera non chiffré

Possible de restaurer 1 volume EBS chiffré à partir de ce snapshot chiffré

Montrer pour le volume EBS chiffré

Snapshot sera chiffré

## Regle entre volume et snapshot et chifffrement

  * Un snapshot prevenant d'un volume non chiffre -----> snapshot non chiffre
  
  * Volume cree a partir d'un snapshot non chiffre peut donner  ----> Volume chiffre

  * Un snapshot chiffre peut etre cree a partir d'un snapshot non chiffre
  
  * Un volume chiffre genere un snapshot chiffre