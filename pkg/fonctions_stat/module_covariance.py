from pkg.fonctions_stat.module_colonne_moyenne import Colonne_moyenne
from pkg.fonctions.module_est_numerique import Est_numerique 
from pkg.fonctions.module_colonne_sans_na import ColonneSansNA
from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat
from pkg.tableaux.module_donnees import Donnees
import config

class Covariance(Fonctions_stat):

    """Classe permettant de calculer la covariance d'une donnée entre deux colonnes.
    
    La classe Covariance prend en attribut une donnée et deux colonnes spécifiées
    par leurs numéros. Elle permet de renvoyer la covariance des valeurs présentes dans
    ces colonnes.

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne sur laquelle on veut appliquer la fonction variance.

    num_colonne1 : int
        Le numero de la première colonne sur laquelle on veut appliquer la fonction covariance.

    num_colonne2 : int
        Le numero de la seconde colonne sur laquelle on veut appliquer la fonction covariance.

    """

    def __init__(self,donnee : Donnees ,num_colonne1 : int ,num_colonne2 : int ):
        self.donnee = donnee 
        self.num_colonne1 = num_colonne1
        self.num_colonne2 = num_colonne2

    def applique(self):

        """La fonction qui permet de calculer la covariance.

        Elle prend en entrée une instance de la classe Covariance
        puis calcule la covariance des colonnes ainsi spécifiées.
        La fonction ignore les valeurs manquantes.

        Returns
        -------
        float
            le résultat du calcul de covariance

        """
        if not (Est_numerique(self.donnee,self.num_colonne1).applique() and Est_numerique(self.donnee,self.num_colonne2).applique()):
            print("erreur_covariance")
            return "erreur"
        else:


            moyX = Colonne_moyenne(self.donnee,self.num_colonne1).applique()
            moyY = Colonne_moyenne(self.donnee,self.num_colonne2).applique()
            indices = []
            for i in range(len(self.donnee.tableau)):
                if (type(self.donnee.tableau[i][self.num_colonne1]) in [int,float]) and (type(self.donnee.tableau[i][self.num_colonne2]) in [int,float]):
                    indices.append(i)

            sum = 0
            for i in indices:
                sum += (self.donnee.tableau[i][self.num_colonne1] - moyX)*(self.donnee.tableau[i][self.num_colonne2] - moyY)
            return sum / len(indices)



