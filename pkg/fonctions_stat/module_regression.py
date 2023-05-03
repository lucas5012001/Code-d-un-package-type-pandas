from turtle import color
from pkg.fonctions_stat.module_fonctions_stat import Fonctions_stat
from pkg.fonctions_stat.module_covariance import Covariance
from pkg.fonctions_stat.module_colonne_moyenne import Colonne_moyenne
from pkg.tableaux.module_donnees import Donnees
from pkg.fonctions.module_faire_liste import Faire_liste
import matplotlib.pyplot as plt

class Regression(Fonctions_stat):

    """Classe permettant de faire une regression linéaire.
    
    La classe Regression prend en attribut une donnée ainsi que
    deux colonnes spécifiées par leurs numéros. Elle réalise alors
    la régréssion linéaire de la seconde colonne par rapport à la
    première. 

    Attributes
    ----------
    donnee : Donnees
        La donnée contenant les variables dont on veut se servir dans la régréssion.

    X : int
        Le numéro de la colonne qui sera en abscisses lors de la régréssion.

    Y : int
        Le numéro de la colonne qui sera en ordonnées lors de la régréssion.

    """
    def __init__(self,donnee : Donnees ,X : int, Y : int, title = False):
        self.donnee = donnee
        self.X = X 
        self.Y = Y 
        self.title = title

    def applique(self):

        """Fonction qui applique réellement la régréssion linéaire.

        Elle prend en entrée une instance de la classe Regression. Elle affiche
        ensuite la régréssion linéaire de la colonne Y par rapport à la colonne
        X. Cette fonction gère les valeurs manquantes dans chacune des deux colonnes
        en les ignorant. Elle permet également d'afficher les informations essentielles
        sur les deux colonnes telles que les variances, moyennes, covariance etc... 
        Elle affiche enfin le résultat de la régréssion sous la forme d'un nuage de points
        et d'une droite de régréssion par l'intermédiaire du module matplotlib.pyplot.
        
        """
        moyX = Colonne_moyenne(self.donnee,self.X).applique()
        moyY = Colonne_moyenne(self.donnee,self.Y).applique()
        CovX_Y = Covariance(self.donnee,self.X,self.Y).applique()
        Var_X = Covariance(self.donnee,self.X,self.X).applique()
        a = CovX_Y/Var_X
        b = moyY - a*moyX
        list_row = []
        for i in range(len(self.donnee.tableau)):
            if ((type(self.donnee.tableau[i][self.X]) in [int,float]) and (type(self.donnee.tableau[i][self.Y]) in [int,float])):
                list_row.append(i)

        droite_reg = [a*self.donnee.tableau[i][self.X] + b for i in list_row]
        ssr = 0
        sst = 0
        j=0
        for i in list_row:
            ssr += (self.donnee.tableau[i][self.Y] - droite_reg[j])**2
            sst += (self.donnee.tableau[i][self.Y] - moyY)**2
            j+=1
        Rcarre = (sst-ssr)/sst
        print("                    ")
        print("Variance de X: "+str(Var_X))
        print("Moyenne de X: "+str(moyX))
        print("                    ")
        print("Variance de Y: "+str(Covariance(self.donnee,self.Y,self.Y).applique()))
        print("Moyenne de Y: "+str(moyY))
        print("                    ")
        print("Cov(X,Y): "+str(CovX_Y))
        print("                    ")
        print("droite: y= " + str(a)+" *x + "+str(b))
        print("R²= "+str(Rcarre))
        X_list= [self.donnee.tableau[i][self.X] for i in list_row]
        Y_list = [self.donnee.tableau[i][self.Y] for i in list_row]
        plt.scatter(X_list,Y_list,color="blue")
        plt.plot(X_list,droite_reg, color = 'red')
        if self.title != False:
            plt.title(self.title)
        plt.show()




