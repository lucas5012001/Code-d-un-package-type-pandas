from pkg.transformations.module_transformations import Transformations
from pkg.tableaux.module_donnees import Donnees
from pkg.fonctions.module_liste_nombre_autre import Liste_nombre_autre

class Tri(Transformations):

    """Classe permettant de trier une donnée selon les valeurs d'une colonne
    
    La classe Tri prend en attribut une donnée et un numero de colonne
    et permet de trier cette donnée par rapport à cette colonne 

    Attributes
    ----------
    donnee : Donnees
        La donnée que l'on veut trier

    colonne : int
        Le numero de la colonne par rapport à laquelle on trie

    Examples
    --------
    >>> data = Donnees([[1,"mq",3],[4,5,6]])
    >>> data.tableau
    [[1, 'mq', 3], [4, 5, 6]]
    >>> a = Tri(data,1)
    >>> a = a.applique()
    >>> a.tableau
    [[4, 5, 6], [1, 'mq', 3]]
    """

    def __init__(self, donnee : Donnees, num_colonne : int = 0):
        self.donnee = donnee
        self.num_colonne = num_colonne

    def applique(self):

        """Transformation qui réalise le Tri.

        Elle prend en entrée une instance de la classe Tri.
        Cette instance permet de caractériser une donnée et
        une de ses colonnes. La fonction trie alors la donnée
        selon cette colonne et renvoie une donnée (de type Donnees).
        Les valeurs manquantes sont prises en charge.

        Returns
        -------
        Donnees
            La donnée triée

        Examples
        --------
        >>> data = Donnees([[1,"mq",3],[4,5,6]])
        >>> data.tableau
        [[1, 'mq', 3], [4, 5, 6]]
        >>> a = Tri(data,1)
        >>> a = a.applique()
        >>> a.tableau
        [[4, 5, 6], [1, 'mq', 3]]
        """
        num_autre = Liste_nombre_autre(self.donnee, self.num_colonne).applique()
        tableau_num = [self.donnee.tableau[i] for i in num_autre[0]]
        tableau_autre = [self.donnee.tableau[i] for i in num_autre[1]]
        liste = [tableau_num[i][self.num_colonne] for i in range(len(tableau_num))]
        indices = list(range(len(liste)))
        for index in range(len(liste)): 
            item = liste[index]         
            j = index
            while j>0 and liste[j-1] > item: 
                liste[j] = liste[j-1]
                indices[j] = indices[j-1]       
                j=j-1
            liste[j]=item   
            indices[j] = index    
        tableau_trie = []
        for ligne1 in indices:
            tableau_trie.append(tableau_num[ligne1])
        tableau_trie += tableau_autre
        if tableau_trie == []:
            self.donnee.tableau = [[]]
        else:
            self.donnee.tableau = tableau_trie
        return self.donnee

