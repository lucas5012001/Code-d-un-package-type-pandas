from pkg.tableaux.module_donnees import Donnees
from pkg.transformations.module_transformations import Transformations

class Modifier(Transformations):
    """Classe permettant de modifier une donnée.
    
    La classe Modifier prend en attribut une donnée, une position
    indiquée par une ligne et une colonne ainsi qu'une valeur à
    entrer à la position spécifiée.

    Attributes
    ----------
    donnee : Donnees
        La donnée sur laquelle on va
        appliquer la modification

    ligne : int
        La ligne sur laquelle va intervenir la modification

    colonne : int
        La colonne sur laquelle va intervenir la modification

    nouvelle_valeur : 
        La valeur à mettre à la position spécifiée.

    """
    def __init__(self,donnee : Donnees,ligne,colonne,nouvelle_valeur):
        self.donnee = donnee 
        self.ligne = ligne 
        self.colonne = colonne 
        self.nouvelle_valeur = nouvelle_valeur

    def applique(self):
        """Transformation qui réalise la modification.

        Elle prend en entrée une instance de la classe Modifier.
        La fonction renvoie ensuite une nouvelle donnée issue de la modification
        de la donnée prise en attribut. Cette donnée est donc identique à une valeur
        près.

        Returns
        -------
        Donnees
            La donnée une fois la modification faite.

        """
        self.donnee.tableau[self.ligne][self.colonne] = self.nouvelle_valeur
        return self.donnee
