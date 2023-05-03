from pkg.transformations.module_transformations import Transformations
from pkg.tableaux.module_donnees import Donnees

class Selection(Transformations):

    """Classe permettant de selectionner des colonnes et des lignes sur
    une donnée.
    
    La classe Selection prend en attribut une donnée, une liste de colonnes à garder,
    une liste de valeurs à conserver sur une colonne et le numero de cette colonne.
    Elle va ensuite permettre de renvoyer une donnée n'ayant plus que les colonnes choisies
    et les lignes dont la valeur dans la colonne spécifiée appartient à la liste de valeurs
    à conserver.

    Attributes
    ----------
    donnee : Donnees
        La donnée sur laquelle on va
        appliquer la selection

    num_colonnes_a_garder : list(int)
        La liste des numeros de colonnes à garder

    supprimer_sur_la_colonne : int
        La colonne sur laquelle on va se baser pour la selection
        de lignes

    supprimer_lignes_differentes_de : list
        Toutes les lignes dont la valeur sur la colonne 
        spécifiée par "supprimer_sur_la_colonne" n'appartient 
        pas à "supprimer_lignes_differentes_de" seront supprimées

    Examples
    --------
    >>> data = Donnees([[1,"mq",3],[4,"a",8],[3,"test",3],[11,5,6]])
    >>> data = Selection(data, [0,2], [3], 2).applique()
    >>> data.tableau
    [[1, 3], [3, 3]]
    """
    def __init__(self, donnee : Donnees, num_colonnes_a_garder : list = [0], supprimer_lignes_differentes_de : list = [], supprimer_sur_la_colonne : int = -1):
        self.donnee = donnee
        self.num_colonnes_a_garder = num_colonnes_a_garder
        self.supprimer_lignes_differentes_de = supprimer_lignes_differentes_de
        self.supprimer_sur_la_colonne = supprimer_sur_la_colonne
        
    def applique(self):

        """Transformation qui réalise la selection.

        Elle prend en entrée une instance de la classe Selection.
        La fonction renvoie ensuite une nouvelle donnée issue de selections
        de lignes et de colonnes sur la donnée en attribut à partir des informations
        placées dans les autres attributs.

        Returns
        -------
        Donnees
            La donnée une fois la selection faite.

        Examples
        --------
        >>> data = Donnees([[1,"mq",3],[4,"a",8],[3,"test",3],[11,5,6]])
        >>> data = Selection(data, [0,2], [3], 2).applique()
        >>> data.tableau
        [[1, 3], [3, 3]]
        """
        if self.supprimer_lignes_differentes_de != [] and self.supprimer_sur_la_colonne != -1:
           liste_a_garder = self.suppr_lignes()
        else:
            liste_a_garder = list(range(len(self.donnee.tableau)))
        if len(self.donnee.colonnes) == len(self.donnee.tableau[0]):
            colonnes = [self.donnee.colonnes[j] for j in self.num_colonnes_a_garder]
        else:
            colonnes = []
        tableau = []
        for i in liste_a_garder:
           tableau.append([self.donnee.tableau[i][j] for j in self.num_colonnes_a_garder])
        return Donnees(tableau, colonnes)

    def suppr_lignes(self):

        """Fonction qui transforme les valeurs à supprimer dans
        une colonne en numéros de lignes à supprimer.

        Returns
        -------
        list
            Numeros de lignes à supprimer.
        """
        liste_a_garder = []
        for i in range(len(self.donnee.tableau)):
            if self.donnee.tableau[i][self.supprimer_sur_la_colonne] in self.supprimer_lignes_differentes_de:
                liste_a_garder.append(i)
        return liste_a_garder
        