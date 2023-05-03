from ast import arguments


class Pipeline:
    """Classe permettant de coordonner l'execution des fonctions du package.
    
    La classe Pipeline prend en attribut une liste de classes et d'arguments
    pour les constructeurs respectifs de ces classes. Elle permet ensuite
    d'executer les fonction applique() de chacune de ces classes dans l'ordre
    indiqué par la liste. Cela permet d'appeler de mutliples fonctions en une
    seule ligne. Notons que le premier element de la liste peut être une donnée
    ou une classe permettant d'en créer une. Les fonctions suivantes s'appliqueront
    alors à cette donnée sans qu'il ne soit nécéssaire de la réintroduire en argument.

    Attributes
    ----------
    ListeFonctionsArguments : list
        La liste des classes (identifiées par abus de langage à leur fonction car elles n'en contiennent qu'une seule)
        et arguments pour les constructeurs des classes.

    Examples
    --------
    >>> conso_gaz_tot=Pipeline([[Simple_Fenetrage,2019,1,2020,1,[1,9],True,["Bretagne"]],[Grouper_somme,0]]).applique()
    """
    def __init__(self,ListeFonctionsArguments):
        self.ListeFonctionsArguments = ListeFonctionsArguments

    def applique(self):
        """La fonction qui permet d'executer les applications
           spécifiées par la liste.

        Elle prend en entrée une instance de la classe Pipeline
        puis execute les fonctions applique() de chacune des classes
        dans le bon ordre. Cette fonction permet de gérer un nombre
        indéterminé de variables en entrée des fonctions grâce au
        préfixe *. De plus, le premier élément de l'attribut 
        ListeFonctionsArguments peut être un objet de type donnée. 
        Dans ce cas, les fonctions suivantes prendront cette donnée 
        en argument.

        Returns
        -------
        dépend des fonctions choisies.

        """
        if len(self.ListeFonctionsArguments[0])==1:
            result = self.ListeFonctionsArguments[0][0]
        else: 
            result = self.ListeFonctionsArguments[0][0](*self.ListeFonctionsArguments[0][1:]).applique()
            
        if len(self.ListeFonctionsArguments) == 1:
            return result
        else:


            for i in range(len(self.ListeFonctionsArguments)-1):
                classe = self.ListeFonctionsArguments[i+1][0]
                args = self.ListeFonctionsArguments[i+1][1:]
                result = classe(result,*args).applique()
            return result