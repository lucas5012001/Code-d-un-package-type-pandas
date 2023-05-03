from pkg.tableaux.module_donnees import Donnees
import gzip
import json
import config

class Import_json(Donnees):

    """Classe permettant d'importer un fichier Json quelconque.
    
    La classe Import_json diffère de la classe DonneesImportees de part
    sa polyvalence. En effet, elle permet de respecter le cahier des charges
    en autorisant l'import de n'importe quel fichier json.gz. Elle prend en
    attributs un chemin et un nom de fichier. La classe DonneesImportees
    reste néammoins plus pratique si les données sont celles qui sont utilisées
    pour le projet car cette dernière réalise toutes les conversions nécéssaires
    de manière automatique.

    Attributes
    ----------
    chemin : str
        Le chemin vers l'emplacement du disque ou se situe le fichier json.gz

    nom_fichier : str
        Le nom du fichier avec son extension json.gz

    """
    
    def __init__(self, chemin, nom_fichier):
        with gzip.open(chemin + nom_fichier, mode='rt', encoding= "UTF-8" ) as gzfile :
                    liste_dico = json.load(gzfile)
        for i in range(len(liste_dico)):
            for key in list(liste_dico[i].keys()):
                if type(liste_dico[i][key]) == dict:
                    liste_dico[i].update(liste_dico[i][key])
                    del liste_dico[i][key]
        cles = []
        for i in range(len(liste_dico)):
            for key in list(liste_dico[i].keys()):
                if not key in cles:
                    cles.append(key)
        data = []       
        for i in range(len(liste_dico)):
            data.append([])
            for colonne in cles:
                data[i].append(liste_dico[i].get(colonne,config.mq_csv))
        self.colonnes = cles 
        self.tableau = data
