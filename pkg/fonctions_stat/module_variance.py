from pkg.fonctions_stat.module_colonne_moyenne import Colonne_moyenne
from pkg.fonctions.module_est_numerique import Est_numerique
from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat 

class Variance(Fonctions_stat):

    """Classe permettant de calculer la variance d'une donnée sur une colonne.
    
    La classe Variance prend en attribut une donnée et une colonne spécifiée
    par son numéro. Elle permet de renvoyer la variance des valeurs présentes dans
    cette colonne.

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant la colonne sur laquelle on veut appliquer la fonction variance.

    num_colonne : int
        Le numero de la colonne sur laquelle on veut appliquer la fonction variance.

    """

    def __init__(self,donnee,num_colonne):
        self.donnee = donnee
        self.num_colonne = num_colonne

    def applique(self):

        """La fonction qui permet de calculer la variance.

        Elle prend en entrée une instance de la classe Variance
        puis calcule la variance de la colonne ainsi spécifiée.
        La fonction ignore les valeurs manquantes.

        Returns
        -------
        float
            le résultat du calcul de variance

        """
        if not Est_numerique(self.donnee,self.num_colonne).applique():

            print("erreur_variance")
            return "erreur"
        else:

            moyX = Colonne_moyenne(self.donnee,self.num_colonne).applique()
            row = []
            for i in range(len(self.donnee.tableau)):
                if type(self.donnee.tableau[i][self.num_colonne]) in [int,float]:

                    row.append(i)
            sum = 0
            for i in row:
                sum += (self.donnee.tableau[i][self.num_colonne] - moyX)**2
            return (sum / len(row))
