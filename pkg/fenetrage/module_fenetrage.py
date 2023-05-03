from pkg.tableaux.module_import import DonneesImportees
from pkg.transformations.module_superposer import Superposer
from pkg.transformations.module_selection import Selection
from pkg.fonctions.module_genere_stations import GenereStations
import config

class Fenetrage:

    """Classe permettant d'importer en une seule ligne un grand nombre de tableaux.
    
    La classe Fenetrage permet d'importer d'une seule ligne tous les tableaux compris entre
    deux dates puis d'appliquer des selections de colonnes et des selections de lignes en fonction
    des régions souhaitées. Cette classe n'est utilisable que pour les données fournies avec le sujet
    de part les fonctionalités liées aux dates et aux régions qui sont propres à nos jeux de données.
    Ce n'est en revanche pas le seul moyen de selectionner ou d'importer des données et cette classe
    est donc contournable si l'utilisateur doit traiter d'autres données.

    Attributes
    ----------
    annee_debut : int
        L'année de début de la sélection.

    mois_debut : int
        Le mois de début de la sélection.

    annee_fin : int
        L'année de fin de la sélection.

    mois_fin : int
        Le mois de fin de la sélection.

    num_colonnes : list[int]
        Les numéros de colonnes à conserver

    csv_True_or_False : bool
        La réponse à la question: Le fichier est un csv.gz ? (sinon il doit être un json.gz)

    regions_a_garder : list[str]
        La liste des régions à conserver

    """


    def __init__(self, annee_debut : int, mois_debut : int, annee_fin : int, moins_fin : int, num_colonnes : list, csv_True_or_False : bool ,regions_a_garder : list = []):

        annee = annee_debut
        mois = mois_debut
        self.liste_annees = []
        self.liste_mois = []
        while annee < annee_fin or (annee == annee_fin and mois <= moins_fin):
            self.liste_annees.append(annee)
            self.liste_mois.append(mois)
            if mois == 12:
                mois = 1
                annee += 1
            else:
                mois +=1
        for i in range(len(self.liste_mois)):
            self.liste_annees[i] = str(self.liste_annees[i])
            if self.liste_mois[i]<10:
                self.liste_mois[i] = "0"+str(self.liste_mois[i])
            else:
                self.liste_mois[i] = str(self.liste_mois[i])
        self.noms_meteo = ["synop." + self.liste_annees[i] + self.liste_mois[i] + ".csv.gz" for i in range(len(self.liste_mois))]
        self.noms_elec = [self.liste_annees[i] + "-" + self.liste_mois[i] + ".json.gz" for i in range(len(self.liste_mois))]
        self.num_colonnes = num_colonnes
        self.csv_True_or_False = csv_True_or_False
        self.regions_a_garder = regions_a_garder


    def applique(self):

        """La fonction qui permet de réaliser l'import et d'executer les
        sélections.

        Elle prend en entrée une instance de la classe fenetrage puis
        importe toutes les données voulues et applique les selections
        voulues. La selection régionale fonctionne pour les deux tables
        bien que la table meteo ne contienne pas de colonne région car
        la fonction applique() établit la liste des stations meteo se
        situant dans la région voulue et selectionne ensuite les lignes
        contenant ces stations meteo. La fonction réalise ensuite la
        supperposition de tous les tableaux importés afin de ne faire
        qu'une seule et même donnée.

        Returns
        -------
        Donnees
            La donnée issue du fenetrage

        """
        if self.csv_True_or_False == True:
            return self.applique_elec()
        else:
            return self.applique_meteo()



    def applique_meteo(self):
        if self.regions_a_garder != []:
            stations_a_garder = GenereStations(self.regions_a_garder,config.chemin_fichier_regions_stations).applique()
        else:
            stations_a_garder = []
        donnees_meteo = None
        for i in range(len(self.liste_mois)):
            if donnees_meteo == None:
                donnees_meteo = Selection(DonneesImportees(config.chemin_meteo, self.noms_meteo[i], True),self.num_colonnes,stations_a_garder,config.index_stations).applique()
            else: 
                donnees_meteo = Superposer(donnees_meteo, Selection(DonneesImportees(config.chemin_meteo, self.noms_meteo[i],True),self.num_colonnes,stations_a_garder,config.index_stations).applique()).applique()

        return donnees_meteo


    def applique_elec(self):
        donnees_elec = None
        for i in range(len(self.liste_mois)):
            if donnees_elec == None:
                donnees_elec = Selection(DonneesImportees(config.chemin_elec, self.noms_elec[i], False), self.num_colonnes,self.regions_a_garder,config.index_regions).applique()
            else: 
                donnees_elec = Superposer(donnees_elec, Selection(DonneesImportees(config.chemin_elec, self.noms_elec[i], False), self.num_colonnes,self.regions_a_garder,config.index_regions).applique()).applique()
        return donnees_elec
    

        

