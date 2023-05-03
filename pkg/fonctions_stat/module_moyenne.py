from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat
from pkg.fonctions_stat.module_colonne_moyenne import Colonne_moyenne
from pkg.tableaux.module_donnees import Donnees

class Moyenne(Fonctions_stat):
    
    """Classe permettant de calculer les moyennes des colonnes d'un tableau
    
    La classe Moyenne permet de faire la moyenne de chaque colonne du tableau de la donnée passée 
    en attribut.
    Elle gère également les valeurs manquantes et renvoie une liste contenant les valeurs des moyennes
    ou la chaine de caractères "non définie" lorsqu'on ne peut pas faire la moyenne.

    Attributes
    ----------
    donnee : Donnees
        La donnee associée au tableau dont on calcule les moyennes

    Examples
    --------
    >>> data = Donnees([[1,2,3],[4,5,6]]) 
    >>> mean = Moyenne(data)
    >>> mean.applique()
    [2.5, 3.5, 4.5]
    """

    def __init__(self, donnee : Donnees):
        self.donnee = donnee

    def applique(self):
        
        """Fonction qui execute réellement les moyennes.

        Elle prend en entrée une instance de la classe Moyenne et retourne
        une liste contenant les moyennes de chaque colonne ou la valeur "non définie"

        Returns
        -------
        list
            liste de moyennes et de chaines de caractères pour les moyennes non définies

        Examples
        --------
        >>> data = Donnees([[1,2,3],[4,5,6]]) 
        >>> mean = Moyenne(data)
        >>> mean.applique()
        [2.5, 3.5, 4.5]
        """

        moyennes = []
        for j in range(len(self.donnee.tableau[0])):
                moyennes.append(Colonne_moyenne(self.donnee, j).applique())
        return moyennes

