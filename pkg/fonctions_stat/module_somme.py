from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat
from pkg.fonctions_stat.module_colonne_somme import Colonne_somme
from pkg.tableaux.module_donnees import Donnees

class Somme(Fonctions_stat):

    """Classe permettant de calculer la somme des valeurs de chaque colonne.
    
    La classe Somme prend en attribut une donnée et permet de faire la somme
    des valeurs du tableau de cette donnée par colonne. 

    Attributes
    ----------
    donnee : Donnees
        La donnée sur laquelle on veut appliquer la somme.

    """

    def __init__(self, donnee : Donnees):
        self.donnee = donnee

    def applique(self):

        """Fonction qui applique réellement la somme par colonne.

        Elle prend en entrée une instance de la classe Somme. Elle
        renvoie ensuite la liste contenant chaque somme des élements de
        chaque colonne ou les mentions "non définie" là ou les sommes
        ne sont pas définies.

        Returns
        -------
        list
            liste des sommes
            
        """

        sommes = []
        for j in range(len(self.donnee.tableau[0])):
                sommes.append(Colonne_somme(self.donnee, j).applique())
        return sommes

