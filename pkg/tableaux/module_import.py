from pkg.tableaux.module_donnees import Donnees
from pkg.transformations.module_conversion_float import Conversion_float 
from pkg.transformations.module_conversion_int import Conversion_int
import gzip
import csv
import json
import config

# Cette classe permet de faire l'importation des données mais aussi de faire toutes les conversions pour gagner du temps.
# Elle est donc dépendante des données car son but est justement de s'y adapter mais pour satisfaire au cahier des charges,
# le programme est concu pour pouvoir se passer de cette classe. En effet, il est possible de se servir des classes
# Import_csv et Import_json pour importer des données quelconques. De plus, cette classe peut facilement être modifiée
# pour pouvoir traiter de nouvelles données à l'aide du fichier config qui permet de faire la plupart des corrections.
# Les seules fonctions qui devront être modifiées à la main sont les fonctions de gestion des dates en cas de changement
# de format concernant ces dernières.


class DonneesImportees(Donnees):

    """Classe permettant d'importer les données'
    
    La classe DonneesImportees permet d'importer les données.
    Elle hérite de la classe Donnees car une donnée importée est considérée
    comme une donnée.

    Attributes
    ----------
    tableau : list(list)
        Le tableau de la donnée

    colonnes : list(str)
        La liste des noms de colonnes

    chemin : str
        chemin d'accès au fichier à importer

    nom_fichier : str
        nom du fichier à importer

    csv_True_or_False : bool
        la variable qui donne le type du fichier à importer

    """

    def __init__(self, chemin, nom_fichier, csv_True_or_False):
        self.chemin = chemin 
        self.nom_fichier = nom_fichier
        self.csv_True_or_False = csv_True_or_False
        if self.csv_True_or_False == True:
            self.import_csv()
        else:
            self.import_json()

    def conversion_meteo(self):
        col_int = config.col_int_meteo
        col_float = config.col_float_meteo
        if col_int != []:
            self.tableau = Conversion_int(self, col_int).applique().tableau
        if col_float != []:
            self.tableau = Conversion_float(self, col_float).applique().tableau

    def conversion_electricite(self):
        col_int = config.col_int_elec
        col_float = config.col_float_elec
        if col_int != []:
            self.tableau = Conversion_int(self, col_int).applique().tableau
        if col_float != []:
            self.tableau = Conversion_float(self, col_float).applique().tableau

    def import_csv(self):
        data = []
        with gzip.open(self.chemin + self.nom_fichier, mode='rt') as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';')
            for row in synopreader :
                data.append(row)
        self.colonnes = data[0][:len(data[0])-1]
        self.tableau = []
        for i in range(1,len(data)):
            self.tableau.append(data[i][:len(data[0])-1])
        self.conversion_meteo()
        self.modif_date_meteo()

    def import_json(self): 
        with gzip.open(self.chemin + self.nom_fichier, mode='rt', encoding= "UTF-8" ) as gzfile :
            liste_dico = json.load(gzfile)
        self.colonnes = config.colonnes_elec
        data = []       
        for i in range(len(liste_dico)):
            data.append([])
            for colonne in self.colonnes:
                data[i].append(liste_dico[i][config.fields_name_elec].get(colonne,config.mq_csv)) 
        self.tableau = data
        self.conversion_electricite()
        self.modif_date_elec()


###################################################################################### 
#            Ces fonctions sont à modifier si les formats de dates changent          #
#            vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv          #
######################################################################################

    def modif_date_meteo(self):
        for ligne in range(len(self.tableau)):
            date_liste = list(self.tableau[ligne][1])[:8]
            date = ""
            for i in range(8):
                date += date_liste[i]
            date = int(date)
            self.tableau[ligne][1] = date

    def modif_date_elec(self):
        for ligne in range(len(self.tableau)):
            date_liste = list(self.tableau[ligne][1])
            date_liste = date_liste[:4] + date_liste[5:7] + date_liste[8:]
            date = ""
            for i in range(8):
                date += date_liste[i]
            date = int(date)
            self.tableau[ligne][1] = date

