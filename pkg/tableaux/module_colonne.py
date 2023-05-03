from pkg.tableaux.module_donnees import Donnees

class Colonne(Donnees):

    """Classe permettant de stocker les colonnes
    
    La classe Colonne hérite de Donnees car une colonne est considérée
    comme un tableau à une seule colonne.

    Attributes
    ----------
    tableau : list(list)
        Le tableau de la donnée

    colonnes : list(str)
        La liste contenant le nom de la colonne

    """

    def __init__(self, liste_donnees : list, nom_colonne : str = ""):
        tableau = [[donnee] for donnee in liste_donnees]
        nom = []
        nom.append(nom_colonne)
        super().__init__(tableau, nom)