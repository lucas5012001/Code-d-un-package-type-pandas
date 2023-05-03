from pkg.fonctions.module_fonctions import Fonctions
from pkg.fonctions.module_faire_liste import Faire_liste
from pkg.tableaux.module_donnees import Donnees

class Unique(Fonctions):

    """Classe permettant de vérifier qu'une colonne est composée de valeurs n'apparaissant qu'une seule fois
    
    La classe Unique permet de vérifier l'abscence de doublons dans une colonne. La colonne est spécifiée
    par une donnée et un numéro de colonne.

    Attributes
    ----------
    donnee : Donnees
        La donnee dans laquelle se trouve la colonne à vérifier

    colonne : int
        Le numéro de la colonne à vérifier

    Examples
    --------
    >>> data = Donnees([[1,2,3],[4,5,6]]) 
    >>> test = Unique(data,1)
    """

    def __init__(self, donnee : Donnees, colonne : int):
        self.donnee = donnee
        self.colonne = colonne
        
    def applique(self):

        """Fonction qui vérifie réellement que la colonne est sans doublons.

        Elle prend en entrée une instance de la classe Unique qui caractérise une
        colonne puis renvoie True si il n'y a pas de doublons et False si il y a
        des doublons

        Returns
        -------
        bool
            réponse a la question: La table n'a aucun doublon ?

        Examples
        --------
        >>> data = Donnees([[1,2,3],[4,5,6]]) 
        >>> test = Unique(data,1)
        >>> test.applique()
        True
        """

        liste = Faire_liste(self.donnee, self.colonne).applique()
        for i in range(len(liste)):
            for j in range(len(liste)):
                if liste[i] == liste[j] and i != j:
                    return False
            return True
                    
        


