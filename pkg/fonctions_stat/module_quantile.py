from pkg.tableaux.module_donnees import Donnees
from pkg.transformations.module_tri import Tri
from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat
import config
class Quantile(Fonctions_stat):

    """Classe permettant d'afficher le quantile d'ordre souhaité de la colonne souhaitée.
    
    La classe Quantile prend en attribut une donnée, une colonne de cette donnée
    spécifiée par son numéro ainsi que l'ordre du quantile souhaité. Elle permet ensuite
    de retourner la valeur de ce quantile.

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne dont on souhaite obtenir un quantile.

    colonne : int
        Le numéro de la colonne dont on souhaite obtenir un quantile.

    quantile : float
        L'ordre compris entre 0 et 1 du quantile que l'on veut.

    """
    def __init__(self,donnee,colonne,quantile):
        self.donnee = donnee
        self.colonne = colonne
        self.quantile = quantile

    def applique(self):

        """Fonction qui renvoie réellement le quantile souhaité.

        Elle prend en entrée une instance de la classe Quantile
        puis renvoie la valeur du quantile souhaité en ignorant les
        valeurs manquantes.

        Returns
        -------
        float
            valeur du quantile
            
        """
        table = Tri(self.donnee,self.colonne).applique().tableau
        n_entrees = len(table)
        n_mq = 0
        for i in range(len(table)):
            if table[i][self.colonne] == config.mq_csv:
                n_mq +=1
        n = n_entrees - n_mq 
        n_obs = int(n*self.quantile)
        valeurs = table[n_obs]
        return Donnees([valeurs],self.donnee.colonnes)

