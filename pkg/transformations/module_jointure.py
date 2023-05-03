from pkg.transformations.module_transformations import Transformations
from pkg.tableaux.module_donnees import Donnees
from pkg.fonctions.module_unique import Unique

class Jointure(Transformations):

    """Classe permettant de joindre deux tables
    
    La classe jointure prend deux données en attribut ainsi
    qu'un numero de colonne par donnée et permet de réaliser
    la jointure des deux tables sur le critère d'égalité des
    valeurs entre ces deux colonnes. La jointure
    doit être faite entre deux colonnes sans doublons.

    Attributes
    ----------
    donnee1 : Donnees
        La première donnée

    donnee2 : Donnees
        La seconde donnée

    colonne1 : int
        Le numero de la colonne de jointure pour la donnee1

    colonne2 : int
        Le numero de la colonne de jointure pour la donnee2

    Examples
    --------
    >>> data1 = Donnees([[1,"mq",3],[4,"a",8],[3,"test",4],[11,7,6]])
    >>> data2 = Donnees([[3,"test",3],[11,5,6]])
    >>> data = Jointure(data1,data2,0,0).applique()
    >>> data.tableau
    [[3, 'test', 4, 3, 'test', 3], [11, 7, 6, 11, 5, 6]]
    """
    
    def __init__(self, donnee1 : Donnees, donnee2 : Donnees, num_col1 : int, num_col2: int):
        self.donnee1 = donnee1
        self.donnee2 = donnee2
        self.num_col1 = num_col1
        self.num_col2 = num_col2

    def applique(self):

        """Transformation qui réalise la jointure.

        Elle prend en entrée une instance de la classe Jointure.
        Elle réalise ensuite la jointure entre les deux données
        prises en attribut et renvoie une nouvelle donnée issue
        de la jointure des deux tableaux selon les colonnes spécifiées
        en attributs.

        Returns
        -------
        Donnees
            La donnée issue de la jointure

        Examples
        --------
        >>> data1 = Donnees([[1,"mq",3],[4,"a",8],[3,"test",4],[11,7,6]])
        >>> data2 = Donnees([[3,"test",3],[11,5,6]])
        >>> data = Jointure(data1,data2,0,0).applique()
        >>> data.tableau
        [[3, 'test', 4, 3, 'test', 3], [11, 7, 6, 11, 5, 6]]
        """
        if not (Unique(self.donnee1,self.num_col1).applique() and Unique(self.donnee2,self.num_col2).applique()):
            return "jointure sur colonnes avec répétitions"
        else:
            liste = []
            for i1 in range(len(self.donnee1.tableau)):
                for i2 in range(len(self.donnee2.tableau)):
                    if self.donnee1.tableau[i1][self.num_col1] == self.donnee2.tableau[i2][self.num_col2]:
                        liste.append([i1,i2])
                        break
            tableau = []
            for couple in liste:
                i1, i2 = couple[0], couple[1]
                tableau.append(self.donnee1.tableau[i1] + self.donnee2.tableau[i2])
            colonnes = self.donnee1.colonnes + self.donnee2.colonnes
            if tableau == []:
                return "Jointure Vide"
            else:
                donnee_jointe = Donnees(tableau, colonnes)
        return donnee_jointe





if __name__ == '__main__':
    import doctest
    doctest.testmod()

    