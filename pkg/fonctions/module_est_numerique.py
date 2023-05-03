from pkg.fonctions.module_fonctions import Fonctions
from pkg.tableaux.module_donnees import Donnees

class Est_numerique(Fonctions):
    
    """Classe permettant de vérifier qu'une colonne est numérique
    
    La classe Est_numerique prend en attribut une donnée et un numero de colonne
    et permet de savoir si la colonne ainsi spécifiée contient au moins un nombre,
    c'est à dire un objet de type int ou float. 

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne que l'on veut vérifier

    colonne : int
        Le numero de la colonne à vérifier

    Examples
    --------
    >>> data = Donnees([[1,"mq",3],[4,5,6]])
    >>> a = Est_numerique(data,1)
    >>> a.applique()
    True
    """

    def __init__(self, donnee : Donnees, colonne : int):
        self.donnee = donnee
        self.colonne = colonne

    def applique(self):

        """Fonction qui fait réellement la vérification.

        Elle prend en entrée une instance de la classe Est_numerique puis
        répond à la question: La colonne contient-elle une valeur numérique ?

        Returns
        -------
        bool
            réponse à la question

        Examples
        --------
        >>> data = Donnees([[1,"mq",3],[4,5,6]])
        >>> a = Est_numerique(data,1)
        >>> a.applique()
        True
        """

        for i in range(len(self.donnee.tableau)):
            if type(self.donnee.tableau[i][self.colonne]) == float or type(self.donnee.tableau[i][self.colonne]) == int:
                return True
        return False