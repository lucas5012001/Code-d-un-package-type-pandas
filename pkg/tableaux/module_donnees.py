class Donnees:

    """Classe permettant de stocker les données
    
    La classe Donnees permet de stocker un tableau sous forme de liste
    de liste ainsi que des noms de colonnes sous forme de liste de chaine de
    caractères.

    Attributes
    ----------
    tableau : list(list)
        Le tableau de la donnée

    colonnes : list(str)
        La liste des noms de colonnes

    """

    def __init__(self, tableau = [[]], colonnes = []):
        self.tableau = tableau
        self.colonnes = colonnes
        