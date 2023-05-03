from pkg.transformations.module_transformations import Transformations
from pkg.fonctions_stat.module_somme import Somme
from pkg.tableaux.module_donnees import Donnees

class Grouper_somme(Transformations):
    """Classe permettant grouper une donnée par somme selon une colonne
    
    La classe Grouper_somme prend une donnée et un numéro de colonne
    en attribut. Elle permet ensuite la réalisation d'une somme
    de chaque colonne pour chaque valeur à l'interieur de la colonne
    prise en attribut. Cela permet d'obtenir une table sans doublons

    Attributes
    ----------
    donnee : Donnees
        La donnée à grouper

    colonne : int
        La colonne selon laquelle on groupe

    """

    def __init__(self, donnee : Donnees, colonne : int):
        self.donnee = donnee
        self.colonne = colonne 

    def applique(self):
        
        """Transformation qui réalise le groupement par somme.

        Elle prend en entrée une instance de la classe Grouper_somme.
        Elle réalise ensuite le groupement par somme selon la colonne 
        spécifiée puis renvoie la donnée groupée

        Returns
        -------
        Donnees
            La donnée issue du groupement

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
            tableau_groupe.append(Somme(Donnees(tableau,self.donnee.colonnes)).applique())
            tableau_groupe[i][self.colonne] = valeurs[i]
        return Donnees(tableau_groupe, self.donnee.colonnes)

