Graphe Formule 1 (2023-2026)

Un graphe sur la Formula 1® contenant des parties de saisons de 2023, 2024, 2025 uniquement dans le but de resté lisible.
Projet réalisé dans le cadre d'un BUT Informatique à l'IUT NFC - UMLP sur le campus de Belfort.
Ce projet consiste à modéliser les relations du championnat de Formule 1 sous forme de graphe et à appliquer plusieurs algorithmes de théorie des graphes.

Le programme construit un graphe reliant :
-> les Années
-> les Grands Prix
-> les Écuries
-> les Pilotes

Puis applique différents algorithmes de parcours et d’analyse.


* Structure du graphe
Chaque type d'entité correspond à un nœud :
   Type         Exemple
  Année	         2024
Grand Prix     Bahrain GP
  Écurie        Ferrari
  Pilote    Charles Leclerc


* Relations représentées par des arêtes :
Année -> Grand Prix
Année -> Écurie
Écurie -> Pilote
Année -> Pilote

Cela permet de représenter l'écosystème complet de la F1 sous forme de graphe.


* Structure du projet
Graphe-F1/
  build_database.py
  projet_graphe_f1.py
  README.md
  data/
    2023.csv
    2024.csv
    2025.csv

  
* Installation
Installer les dépendances Python (uniquement si besoin) :
'pip3 install pandas networkx matplotlib requests' (attention la commande peut varier)
(commande utilisée sur : macOS Tahoe 26.3.1)


* Génération de la base de données
Le script build_database.py télécharge les données depuis une API de statistiques F1 et génère les fichiers CSV.

Lancer :
'python3 build_database.py'

Cela crée les fichiers :
data/2023.csv
data/2024.csv
data/2025.csv

Chaque fichier contient :
-> colonne	description
-> year	année
-> grand_prix	nom du GP
-> team	écurie
-> engine motoriste
-> pilot	pilote
-> replacement	remplacement éventuel


* Exécution du programme
Lancer le programme principal :
'python3 projet_graphe_f1.py'

Le programme :
-> construit le graphe
-> affiche des statistiques
-> exécute différents algorithmes
-> affiche la visualisation du graphe

* Algorithmes utilisés
-> BFS (Breadth First Search)
   Parcours du graphe en largeur.
   - Permet d’explorer les relations entre les entités du championnat.

-> DFS (Depth First Search)
   Parcours en profondeur du graphe.
   - Permet d’explorer les chemins possibles dans le réseau.

-> Dijkstra
   Algorithme de plus court chemin entre deux nœuds.
   Exemple :
   - Lewis Hamilton_2020 -> Mercedes
      distance = 1
   ou
   - Pierre Gasly_2020 → AlphaTauri → Honda
      distance = 2


* Statistiques calculées
Le programme détermine également :
-> l’année avec le plus de pilotes
-> l’année avec le moins de pilotes
-> l’année avec le plus de Grands Prix
-> l’année avec le moins de Grands Prix
-> l’année avec le plus de motoristes
-> l’année avec le moins de motoristes


* Visualisation
Le graphe est affiché avec NetworkX et Matplotlib.
-> Couleurs utilisées :
  Couleur    Type
🔵 bleu	     année
🔴 rouge     écurie
🟣 violet	 grand prix
🟢 vert	     pilote

* Objectifs du projet
-> Manipulation de structures de graphes
-> Implémentation d’algorithmes classiques
-> Analyse de données sportives
-> Visualisation de graphes complexes


* Technologies utilisées :
-> Python
-> NetworkX
-> Pandas
-> Matplotlib


* Sources des données
Les données sont récupérées via une API publique de statistiques F1.


* Auteur
Lucas FRICHET
Étudiant IUT NFC - UMLP
BUT1 Informatique
Belfort, 90000

(Mise en forme fait automatique et ne correspond pas à mes souhaits et à ce que j'ai fais)
