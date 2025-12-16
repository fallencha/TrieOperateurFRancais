# TrieOp-rateurFRan-ais
Script Python permettant de trier une grande liste de numéros français en fonction de l'opérateur ,les ranges dans un dossier (resultats) ,avec la possibilité de checker des numéros directement de façon individuel.


-Trie les numéros selon les préfixes attribués aux 4 opérateurs (Orange, SFR, Bouygues, Free).

-Enregistre les résultats dans des fichiers séparés (Orange.txt, SFR.txt, Bouygues.txt, Free.txt, AutreOperateur.txt).

-Permet de choisir entre lecture d’un fichier .txt ou saisie manuelle.

-Affiche un résumé statistique du nombre de numéros trouvés par opérateur.
-tes numéros peuvent arriver sous plusieurs formats :

0033XXXXXXXXX

+33XXXXXXXXX

33XXXXXXXXX

ou directement 0XXXXXXXXX

👉 Dans tous les cas, il faut ignorer l’indicatif international (33) et ne garder que la partie nationale commençant par 0. Par exemple :

00333768151190 → devient 0768151190

+33768151190 → devient 0768151190

33768151190 → devient 0768151190

0768151190 → reste 0768151190
