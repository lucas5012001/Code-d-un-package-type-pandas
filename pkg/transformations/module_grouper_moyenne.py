from pkg.transformations.module_transformations import Transformations
from pkg.fonctions_stat.module_moyenne import Moyenne
from pkg.tableaux.module_donnees import Donnees

class Grouper_moyenne(Transformations):

    """Classe permettant grouper une donnée par moyenne selon une colonne.
    
    La classe Grouper_moyenne prend une donnée et un numéro de colonne
    en attribut. Elle permet ensuite la réalisation d'une moyenne
    de chaque colonne pour chaque valeur à l'interieur de la colonne
    prise en attribut. Cela permet d'obtenir une table sans doublons

    Attributes
    ----------
    donnee : Donnees
        La donnée à grouper

    colonne : int
        La colonne selon laquelle on groupe.

    Examples
    --------
    >>> data = Donnees([[1,"mq",3],[4,"a",8],[3,"test",4],[11,7,6],[8,"mq",4]])
    >>> data = Grouper_moyenne(data,1).applique()
    >>> data.tableau
    [[4.5, 'mq', 3.5], [4.0, 'a', 8.0], [3.0, 'test', 4.0], [11.0, 7, 6.0]]
    """
    def __init__(self, donnee : Donnees, colonne : int):
        self.donnee = donnee
        self.colonne = colonne 

    def applique(self):

        """Transformation qui réalise le groupement.

        Elle prend en entrée une instance de la classe Grouper_moyenne.
        Elle réalise ensuite le groupement selon la colonne 
        spécifiée puis renvoie la donnée groupée

        Returns
        -------
        Donnees
            La donnée issue du groupement

        Examples
        --------
        >>> data = Donnees([[1,"mq",3],[4,"a",8],[3,"test",4],[11,7,6],[8,"mq",4]])
        >>> data = Grouper_moyenne(data,1).applique()
        >>> data.tableau
        [[4.5, 'mq', 3.5], [4.0, 'a', 8.0], [3.0, 'test', 4.0], [11.0, 7, 6.0]]
        """
        valeurs = [self.donnee.tableau[i][self.colonne] for i in range(len(self.donnee.tableau))]
        valeurs = list(set(valeurs))
        indices = []
        for val in valeurs:
            liste = []
            for ligne in range(len(self.donnee.tableau)):
                if self.donnee.tableau[ligne][self.colonne] == val:
                    liste.append(ligne)
            indices.append(liste)
        tableau_groupe = []
        for i in range(len(valeurs)):
            tableau = [self.donnee.tableau[ligne] for ligne in indices[i]]
            tableau_groupe.append(Moyenne(Donnees(tableau,self.donnee.colonnes)).applique())
            tableau_groupe[i][self.colonne] = valeurs[i]
        return Donnees(tableau_groupe, self.donnee.colonnes)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
