import config
from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat
from pkg.tableaux.module_donnees import Donnees
from pkg.fonctions.module_est_numerique import Est_numerique

class Colonne_moyenne(Fonctions_stat):

    """Classe permettant de faire la moyenne d'une colonne numérique
    
    La classe Colonne_moyenne prend en attribut une donnée et un numero de colonne
    et permet de calculer la moyenne sur la colonne ainsi spécifiée.
    Le processus intègre la gestion des valeurs manquantes.

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne sur laquelle on veut
        faire la moyenne

    colonne : int
        Le numero de la colonne sur laquelle on veut faire
        la moyenne.

    Examples
    --------
    >>> data = Donnees([[1,"mq",3],[4,5,6],[3,7,7]])
    >>> a = Colonne_moyenne(data,1)
    >>> a.applique()
    >>> a
    6.0
    """

    def __init__(self, donnee : Donnees, num_colonne : int):
        self.donnee = donnee 
        self.num_colonne = num_colonne 

    def applique(self):

        """Fonction qui fait réellement la moyenne sur la colonne.

        Elle prend en entrée une instance de la classe Colonne_moyenne puis
        fait la moyenne sur la colonne ainsi spécifiée. Elle renvoie "non définie"
        si il n'est pas possible de faire la moyenne (pas de valeurs numériques)

        Returns
        -------
        float
            La moyenne de la colonne

        str
            "non définie" si la moyenne n'existe pas 

        Examples
        --------
        >>> data = Donnees([[1,"mq",3],[4,5,6],[3,7,7]])
        >>> a = Colonne_moyenne(data,1)
        >>> a.applique()
        >>> a
        6.0
        """

        if not Est_numerique(self.donnee, self.num_colonne).applique():
            return "non définie"
        compteur = 0
        sum = 0
        for i in range(len(self.donnee.tableau)):
            if self.donnee.tableau[i][self.num_colonne] == config.mq_csv : 
                pass
            elif type(self.donnee.tableau[i][self.num_colonne]) == float or type(self.donnee.tableau[i][self.num_colonne]) == int:
                sum += self.donnee.tableau[i][self.num_colonne]
                compteur += 1
            else:
                return "non définie"
        return sum/compteur
