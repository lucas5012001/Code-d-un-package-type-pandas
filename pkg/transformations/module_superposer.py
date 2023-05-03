from pkg.transformations.module_transformations import Transformations
from pkg.tableaux.module_donnees import Donnees

class Superposer(Transformations):

    """Classe permettant de superposer les tableaux de deux données
    
    La classe Superposer prend en attribut deux données et permet de
    superposer les tableaux de ces données pour renvoyer une nouvelle
    donnée dont le tableau est le resultat de cette superposition.

    Attributes
    ----------
    donnee1 : Donnees
        La première donnée

    donnee2 : Donnees
        La seconde donnée

    Examples
    --------
    >>> data1 = Donnees([[1,"mq",3],[4,"a",8]])
    >>> data2 = Donnees([[3,"test",3],[11,5,6]])
    >>> superposition = Superposer(data1,data2).applique()
    >>> superposition.tableau
    [[1, 'mq', 3], [4, 'a', 8], [3, 'test', 3], [11, 5, 6]]
    """
    
    def __init__(self, donnee1 : Donnees, donnee2 : Donnees):
        self.donnee1 = donnee1
        self.donnee2 = donnee2

    def applique(self):

        """Transformation qui réalise la superposition.

        Elle prend en entrée une instance de la classe Superposer.
        Cette instance permet de caractériser un couple de données. 
        La transformation superpose alors les tableaux de données et 
        renvoie une nouvelle donnée (de type Donnees) faite
        à partir de cette superposition.

        Returns
        -------
        Donnees
            La donnée issue de la superposition

        Examples
        --------
        >>> data1 = Donnees([[1,"mq",3],[4,"a",8]])
        >>> data2 = Donnees([[3,"test",3],[11,5,6]])
        >>> superposition = Superposer(data1,data2).applique()
        >>> superposition.tableau
        [[1, 'mq', 3], [4, 'a', 8], [3, 'test', 3], [11, 5, 6]]
        """
        return Donnees(self.donnee1.tableau + self.donnee2.tableau, self.donnee1.colonnes)


if __name__ == '__main__':
    import doctest
    doctest.testmod()