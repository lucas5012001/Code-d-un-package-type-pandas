from pkg.fonctions.module_fonctions import Fonctions
import csv
class GenereStations(Fonctions):

    """Classe permettant de trouver les numeros de stations appartenant à un ensemble de régions.
    
    La classe GenereStations prend comme attribut une liste de régions et sert à obtenir la liste des 
    stations appartenant à l'une de ces régions.

    Attributes
    ----------
    liste_regions : list(str)
        La liste des régions

    chemin : str
        Chemin d'accès au fichier postesSynopAvecRegions.csv

    Examples
    --------
    >>> a=GenereStations(["Normandie"],"P:/projet info/python/donnees/Fichiers de Données .csv.gz-20220504/")
    >>> a.applique()
    ['07020', '07027', '07037', '07139']
    """

    def __init__(self, liste_regions, chemin):
        self.nom_fichier = "postesSynopAvecRegions.csv"
        self.chemin = chemin
        data = []
        with open(self.chemin + self.nom_fichier, mode='rt', encoding= "UTF-8") as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';')
            for row in synopreader :
                data.append(row)
        self.tableau = [[data[i][0],data[i][5]] for i in range(1,len(data))]
        liste_stations = []
        for region in liste_regions:
            for ligne in range(len(self.tableau)):
                if self.tableau[ligne][1] == region:
                    liste_stations.append(self.tableau[ligne][0])
        self.liste_stations = liste_stations

    def applique(self):
        """Fonction qui renvoie la liste de stations.

        La liste de stations a été calculée directement dans le 
        __init__ mais il faut faire appel à cette fonction pour
        retourner cette liste.

        Returns
        -------
        list(str)
            liste de des stations appartenant à l'ensemble de
            régions spécifié en attribut

        Examples
        --------
        >>> a=GenereStations(["Normandie"],"P:/projet info/python/donnees/Fichiers de Données .csv.gz-20220504/")
        >>> a.applique()
        ['07020', '07027', '07037', '07139']
        """
        return self.liste_stations

