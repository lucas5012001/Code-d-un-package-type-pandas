from pkg.fonctions.module_fonctions import Fonctions
from pkg.tableaux.module_donnees import Donnees

class Liste_nombre_autre(Fonctions):

    """Classe permettant de récupérer les indices d'une colonne ou se trouvent des nombres
    et les indices ou se trouvent d'autres objets.
    
    La classe Liste_nombre_autre permet de balayer les indices d'une colonne pour obtenir les positions
    ou se trouvent des nombres (int ou float), obtenir les positions ou se trouvent des objets d'autres types,
    puis renvoyer ces positions dans une liste de deux listes.

    Attributes
    ----------
    donnee : Donnees
        La donnee à laquelle appartient la colonne balayée

    colonne : int
        le numero de la colonne à balayer

    Examples
    --------
    >>> data = Donnees([[1,"val",3],[4,5,6]]) 
    >>> L = Liste_nombre_autre(data,1)
    >>> [nombre,autre] = L.append()
    >>> nombre
    [1]
    """

    def __init__(self, donnee : Donnees, colonne : int):
        self.donnee = donnee
        self.colonne = colonne
        
    def applique(self):

        """Fonction crée réellement les listes d'indices.

        Elle prend en entrée une instance de la classe Liste_nombre_autre()
        et renvoie les listes d'indices ou se trouvent les nombres et les autres
        types d'objets 

        Returns
        -------
        list(list)
            liste de deux listes: la premiere contient les indices de nombres
            la deuxieme contient les indices des autres types

        Examples
        --------
        >>> data = Donnees([[1,"val",3],[4,5,6]]) 
        >>> L = Liste_nombre_autre(data,1)
        >>> [nombre,autre] = L.append()
        >>> nombre
        [1]
        """
        nombre = []
        autre = []
        for i in range(len(self.donnee.tableau)):
            if type(self.donnee.tableau[i][self.colonne]) == int or type(self.donnee.tableau[i][self.colonne]) == float:
                nombre.append(i)
            else:
                autre.append(i)
        return([nombre,autre])

        