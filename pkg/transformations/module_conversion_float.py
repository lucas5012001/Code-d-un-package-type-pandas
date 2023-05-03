from pkg.transformations.module_transformations import Transformations
from pkg.tableaux.module_donnees import Donnees
import config

class Conversion_float(Transformations):

    """Classe permettant convertir une colonne de donnée de type str en float
    
    La classe Conversion_float prend en attribut une donnée et un numero pour
    spécifier une colonne de cette donnée. Elle permet ensuite de convertir
    cette colonne du type str vers le type float.

    Attributes
    ----------
    donnee : Donnees
        La donnée qui contient la colonne à convertir

    colonne : int
        La colonne à convertir

    Examples
    --------
    >>> data = Donnees([["1","mq","3"],["4","a","8"],["3","test","4"],["11","7","6"]])
    >>> data = Conversion_float(data,[0]).applique()
    >>> data.tableau
    [[1.0, 'mq', '3'], [4.0, 'a', '8'], [3.0, 'test', '4'], [11.0, '7', '6']]
    """
    
    def __init__(self, donnee : Donnees, liste_colonnes : list = [0]):
        self.donnee = donnee
        self.liste_colonnes = liste_colonnes

    def applique(self):

        """Transformation qui réalise la conversion.

        Elle prend en entrée une instance de la classe Colonne_float.
        Elle réalise ensuite la conversion de la colonne spécifiée
        depuis le format str vers le format float.

        Returns
        -------
        Donnees
            La donnée issue de la conversion

        Examples
        --------
        >>> data = Donnees([["1","mq","3"],["4","a","8"],["3","test","4"],["11","7","6"]])
        >>> data = Conversion_int(data,[0]).applique()
        >>> data.tableau
        [[1.0, 'mq', '3'], [4.0, 'a', '8'], [3.0, 'test', '4'], [11.0, '7', '6']]
        """

        for colonne in self.liste_colonnes:
            for ligne in range(len(self.donnee.tableau)):
                if (self.donnee.tableau[ligne][colonne]) != config.mq_csv:
                    self.donnee.tableau[ligne][colonne] = float(self.donnee.tableau[ligne][colonne])
        return self.donnee
