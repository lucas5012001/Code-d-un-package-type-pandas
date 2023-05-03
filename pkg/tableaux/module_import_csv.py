from pkg.tableaux.module_donnees import Donnees
import gzip
import csv

class Import_csv(Donnees):

    """Classe permettant d'importer un fichier Json quelconque.
    
    La classe Import_csv diffère de la classe DonneesImportees de part
    sa polyvalence. En effet, elle permet de respecter le cahier des charges
    en autorisant l'import de n'importe quel fichier csv.gz. Elle prend en
    attributs un chemin et un nom de fichier. La classe DonneesImportees
    reste néammoins plus pratique si les données sont celles qui sont utilisées
    pour le projet car cette dernière réalise toutes les conversions nécéssaires
    de manière automatique.

    Attributes
    ----------
    chemin : str
        Le chemin vers l'emplacement du disque ou se situe le fichier csv.gz

    nom_fichier : str
        Le nom du fichier avec son extension csv.gz
        
    """

    def __init__(self, chemin, nom_fichier):
        data = []
        with gzip.open(chemin + nom_fichier, mode='rt') as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';')
            for row in synopreader :
                data.append(row)
        self.colonnes = data[0]
        self.tableau = data[1:]
