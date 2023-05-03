from pkg.fonctions.module_fonctions import Fonctions
from pkg.tableaux.module_donnees import Donnees
import config

class ColonneSansNA(Fonctions):

    """Classe permettant de vérifier qu'une colonne ne contient pas de valeurs manquantes.
    
    La classe ColonneSansNA prend en attribut une donnée et une colonne de cette donnée
    spécifiée par son numéro. Elle permet ensuite de vérifier si la colonne contient des
    valeurs manquantes ou non en renvoyant True si il n'y en a pas et False si des valeurs manquent.

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne sur laquelle on veut faire la vérification.

    num_colonne : int
        Le numero de la colonne à vérifier.

    """
    def __init__(self,donnee : Donnees ,num_colonne : int):
        self.donnee = donnee 
        self.num_colonne = num_colonne

    def applique(self):

        """Fonction qui fait réellement la vérification.

        Elle prend en entrée une instance de la ColonneSansNA.
        Elle renvoie True si il n'y a pas de valeurs manquantes et
        False si il y a des valeurs manquantes.

        Returns
        -------
        bool
            Le résultat de la vérification

        """
        for i in range(len(self.donnee.tableau)):
            if self.donnee.tableau[i][self.num_colonne] == config.mq_csv:
                return False 
        return True
