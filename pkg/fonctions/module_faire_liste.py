from pkg.fonctions.module_fonctions import Fonctions
from pkg.tableaux.module_donnees import Donnees

class Faire_liste(Fonctions):

    """Classe permettant de transformer une colonne d'une donnée en liste.
    
    La classe Faire_liste prend en attribut une donnée et un numero de colonne
    et permet d'obtenir une liste constituée des éléments de la colonne ainsi 
    spécifiée.

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne avec laquelle on veut
        faire une liste.

    colonne : int
        Le numero de la colonne avec laquelle on veut faire une liste.
        
    Examples
    --------
    >>> data = Donnees([[1,2,3],[4,5,6]])
    >>> a = Faire_liste(data,1)
    >>> a.applique()
    [2, 5]
    """

    def __init__(self, donnee : Donnees, colonne : int):
        self.donnee = donnee
        self.colonne = colonne

    def applique(self):

        """Fonction qui fait réellement la liste.

        Elle prend en entrée une instance de la classe Faire_liste puis
        crée une liste à partir des éléments de la colonne spécifiée par
        l'instance.

        Returns
        -------
        list
            La liste de valeurs

        Examples
        --------
        >>> data = Donnees([[1,2,3],[4,5,6]])
        >>> a = Faire_liste(data,1)
        >>> a.applique()
        [2, 5]
        """

        liste = [self.donnee.tableau[i][self.colonne] for i in range(len(self.donnee.tableau))]
        return liste
