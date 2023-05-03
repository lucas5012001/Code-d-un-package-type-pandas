Projet traitement de données, Ensai, 1A, rendu le 30/05/2022.

#######################################################
#    Anaïs DUMAS, Marie-Anaïs VERDIN, Lucas LALOUE    #
#######################################################

Création d’une application python permettant de faire le lien entre des données météorologiques et des données de consommation énergétique. L’application doit permettre à l’utilisateur d’importer et mettre en forme les données de son choix puis lui permettre de les analyser avec des outils statistiques intégrés à l’application.

###############################################################################################
Il est très important de modifier les lignes 8,9,10 du fichier config.py pour utiliser main.py.
###############################################################################################


Ce package permet d'importer des données depuis des formats json.gz ou csv.gz, de les transformer, traiter,
analyser puis éventuellement de les enregistrer sur le disque dur et de les modifier. Il est concu pour
traiter n'importe quel type de données.

Le package contient deux modules qui dépendent des données fournies avec le sujet : le module Import et le module Fenetrage.
Cela ne pose pas de probleme car ces deux modules permettent simplement d'aller plus vite lorsqu'on traite
les données fournies avec le sujet mais ils ne font qu'executer des fonctions accessibles manuellement et peuvent donc être contournés
par l'utilisateur si il doit traiter d'autres données. En effet, le module Import peut être contourné en utilisant successivement
soit le module Import_csv soit le module Import_json puis les modules Conversion_int et Conversion_float.
Le module fenetrage peut lui être contourné par une succession d'import_json ou Import_csv et de selections.
Aucune fonctionnalité si ce n'est la selection par region des données meteo n'est donc exclusive aux données du sujet.
Cela s'explique par la nécéssité d'utiliser un fichier tiers pour selectionner les regions dans les tables meteo etant
donné l'abscence de colonne région dans ces tables. On remarque cependant que le module selection permettrait de
faire une selection régionale (ou sur toute autre variable qualitative) sur n'importe quel fichier à condition
que celui ci contienne une colonne région (ou autre variable sur laquelle on fait la selection).