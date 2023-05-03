from pkg.transformations.module_transformations import Transformations
from pkg.tableaux.module_donnees import Donnees
from pkg.fonctions_stat.module_moyenne import Moyenne

class Centrage(Transformations):

    """Classe permettant de centrer les données
    
    La classe Centrage prend en attribut une donnée. Elle permet ensuite de centrer
    le tableau de cette donnée, c'est à dire de retrancher la moyenne de chaque colonne
    aux valeurs qui la composent. Les colonnes non numériques ne sont pas modifiées.

    Attributes
    ----------
    donnee : Donnees
        La donnée dont le tableau doit être centré

    Examples
    --------
    >>> data = Donnees([[1,"mq",3],[4,5,8],[3,"test",4],[11,7,6]])
    >>> data = Centrage(data).applique()
    >>> data.tableau
    [[-3.75, 'mq', -2.25], [-0.75, 5, 2.75], [-1.75, 'test', -1.25], [6.25, 7, 0.75]]
    """

    def __init__(self, donnee : Donnees):
        self.donnee = donnee

    def applique(self):

        """Transformation qui réalise le centrage.

        Elle prend en entrée une instance de la classe Centrage.
        Elle réalise ensuite le centrage de la donnée qui est en
        attribut. Les colonnes non numériques ne sont pas modifiées.

        Returns
        -------
        Donnees
            La donnée centrée

        Examples
        --------
        >>> data = Donnees([[1,"mq",3],[4,5,8],[3,"test",4],[11,7,6]])
        >>> data = Centrage(data).applique()
        >>> data.tableau
        [[-3.75, 'mq', -2.25], [-0.75, 5, 2.75], [-1.75, 'test', -1.25], [6.25, 7, 0.75]]
        """
        j = 0
        for j,moy in enumerate(Moyenne(self.donnee).applique()):
            if moy == 'non définie':
                pass
            elif type(moy) == int or type(moy) == float:
                for i in range(len(self.donnee.tableau)):
                    if type(self.donnee.tableau[i][j]) == int or type(self.donnee.tableau[i][j]) == float:
                        self.donnee.tableau[i][j] = self.donnee.tableau[i][j] - moy
            else:
                return("erreur")
        return(self.donnee)

