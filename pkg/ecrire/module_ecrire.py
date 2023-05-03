from pkg.tableaux.module_donnees import Donnees
import csv
class Ecrire:

    """Classe permettant de créer un fichier au format csv sur le disque.

    Attributes
    ----------
    donnee : Donnees
        La donnée à partir de laquelle on va créer un fichier csv

    dossier : str
        Le dossier dans lequel on veut enregistrer le fichier csv

    nom_fichier_a_ecrire : str
        Le nom du fichier qui va être enregistré (sans son extension .csv)

    """
    def __init__(self,donnee : Donnees,dossier,nom_fichier_a_ecrire):
        self.donnee = donnee
        self.dossier = dossier
        self.nom_fichier_a_ecrire = nom_fichier_a_ecrire

    def applique(self):

        """La fonction qui permet de réaliser l'enregistrement du
        fichier.

        Elle prend en entrée une instance de Ecrire puis elle enregistre
        la donnée sur le disque au chemin spécifié, avec le nom spécifié
        au format csv.

        """

        list = []
        list.append(self.donnee.colonnes)
        for row in self.donnee.tableau:
            list.append(row)
        with open(self.dossier+self.nom_fichier_a_ecrire+'.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
            writer.writerows(list)