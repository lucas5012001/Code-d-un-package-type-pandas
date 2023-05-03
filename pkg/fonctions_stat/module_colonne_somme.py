import config
from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat
from pkg.tableaux.module_donnees import Donnees
from pkg.fonctions.module_est_numerique import Est_numerique

class Colonne_somme(Fonctions_stat):

    """Classe permettant de faire la somme d'une colonne numérique
    
    La classe Colonne_somme prend en attribut une donnée et un numero de colonne
    et permet de calculer la somme sur la colonne ainsi spécifiée.
    Le processus intègre la gestion des valeurs manquantes.

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne sur laquelle on veut
        faire la somme

    colonne : int
        Le numero de la colonne sur laquelle on veut faire
        la somme.

    """

    def __init__(self, donnee : Donnees, num_colonne : int):
        self.donnee = donnee 
        self.num_colonne = num_colonne 

    def applique(self):

        """Fonction qui fait réellement la somme sur la colonne.

        Elle prend en entrée une instance de la classe Colonne_somme puis
        fait la somme sur la colonne ainsi spécifiée. Elle renvoie "non définie"
        si il n'est pas possible de faire la somme (pas de valeurs numériques)

        Returns
        -------
        float
            La somme de la colonne

        str
            "non définie" si la somme n'existe pas 

        """

        if not Est_numerique(self.donnee, self.num_colonne).applique():
            return "non définie"
        sum = 0
        for i in range(len(self.donnee.tableau)):
            if self.donnee.tableau[i][self.num_colonne] == config.mq_csv : 
                pass
            elif type(self.donnee.tableau[i][self.num_colonne]) == float or type(self.donnee.tableau[i][self.num_colonne]) == int:
                sum += self.donnee.tableau[i][self.num_colonne]
            else:
                return "non définie"
        return sum
