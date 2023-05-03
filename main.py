from pkg.fonctions_stat.module_colonne_moyenne import Colonne_moyenne
from pkg.transformations.module_conversion_float import Conversion_float
from pkg.transformations.module_grouper_somme import Grouper_somme
from pkg.transformations.module_tri import Tri
from pkg.fenetrage.module_fenetrage import Fenetrage
from pkg.transformations.module_jointure import Jointure
from pkg.transformations.module_grouper_moyenne import Grouper_moyenne
from pkg.pipeline.module_pipeline import Pipeline
from pkg.fonctions_stat.module_regression import Regression
from pkg.fonctions.module_faire_liste import Faire_liste
from pkg.fonctions_stat.module_covariance import Covariance
from pkg.tableaux.module_import_csv import Import_csv
from pkg.tableaux.module_import_json import Import_json
from pkg.ecrire.module_ecrire import Ecrire
from pkg.transformations.module_modifier import Modifier
import matplotlib.pyplot as plt
import config

#######################################################################################################################################################################
# Pour utiliser le code ci-dessous, il faut modifier les chemins d'accès aux données météo, électricité et au dossier contenant le fichier postesSynopAvecRegions.csv #
# dans le module config.py lignes 8,9,10.                                                                                                                                           #
# Il est également possible d'importer d'autres données csv ou json avec les classes Import_csv et Import_json.                                                                       #
#######################################################################################################################################################################

questions_a_executer = [1,2,3,4,5,6,7] # Entrer ici les numeros des questions à executer.


if config.chemin_elec == None or config.chemin_meteo == None or config.chemin_fichier_regions_stations == None:
    print("Modifier les chemins d'acces aux fichiers dans le dossier config.py lignes 8,9,10")
    questions_a_executer = []


######## Debut des questions #########
######################################

if 1 in questions_a_executer:
    ################################################################################### QUESTION 1
    # En bretagne, la consommation de gaz est elle impactée par la température ?
    conso_gaz_tot=Pipeline([[Fenetrage,2021,1,2021,12,[1,9],True,["Bretagne"]],[Grouper_somme,0]]).applique() # Importe la table ELEC entre 01/2021 et 12/2021 en gardant les variables 
                                                                                                # Date et Conso gaz brute. Conserve uniquement les entrées qui proviennent de Bretagne
                                                                                                # Groupe ensuite par date en sommant (aggrégation).

    meteo=Pipeline([[Fenetrage,2021,1,2021,12,[1,7],False,["Bretagne"]],[Grouper_moyenne,0]]).applique()# Importe la table METEO entre 01/2021 et 12/2021 en gardant les variables 
                                                                                                # Date et température. Conserve uniquement les entrées qui proviennent de Bretagne
                                                                                                # Groupe ensuite par date en faisant la moyenne (aggrégation).

    Pipeline([[Jointure,conso_gaz_tot,meteo,0,0],[Tri,3],[Regression,3,1,"Consommation de gaz en fonction de la température en Bretagne"]]).applique() # Jointure des deux tables, tri croissant en fonction de la colonne température
                                                                                                                                                       # Puis tracé d'une régréssion linéaire avec X = température, Y = Conso gaz brute


if 2 in questions_a_executer:
    ################################################################################### QUESTION 2
    # L'année 2021 a t elle été plus chaude en Bretagne qu'en Normandie ?
    # Combien de degrés d'écart ?
    # Temperature moyenne en france en 2021 ? 
    temperature_bretagne=Pipeline([[Fenetrage,2021,1,2021,12,[7],False,["Bretagne"]],[Colonne_moyenne,0]]).applique() # Temperature moyenne en Bretagne pour l'année
                                                                                                                             # 2021
    temperature_normandie = Pipeline([[Fenetrage,2021,1,2021,12,[7],False,["Normandie"]],[Colonne_moyenne,0]]).applique() # Temperature moyenne en Normandie pour l'année
                                                                                                                                 # 2021
    moyenne_france = Pipeline([[Fenetrage,2021,1,2021,12,[7],False],[Colonne_moyenne,0]]).applique() 

    print("plus chaud en bretagne qu'en normandie ?")
    print(temperature_bretagne > temperature_normandie) # booléen
    print("           ")
    print("Combien de degrés d'écart ? ")
    print(round(abs(temperature_bretagne - temperature_normandie),2)) # Les degrés sont en kelvin mais la différence ne change pas et peut etre lue en degrés celsius.
    print("          ")
    print("temperature moyenne en France en 2021?")
    print(round(moyenne_france - 273.15,2))


if 3 in questions_a_executer:
    ################################################################################### QUESTION 2
    # Comparer les évolutions de températures des années 2020 et 2021
    evol_temperature_2020= Pipeline([[Fenetrage,2020,1,2020,12,[1,7],False],[Grouper_moyenne,0],[Tri,0],[Faire_liste,1]]).applique()
    evol_temperature_2021 = Pipeline([[Fenetrage,2021,1,2021,12,[1,7],False],[Grouper_moyenne,0],[Tri,0],[Faire_liste,1]]).applique()
    plt.plot(evol_temperature_2020)
    plt.plot(evol_temperature_2021)
    plt.legend(['température année 2020', 'température année 2021'])
    plt.axis()
    plt.show()


if 4 in questions_a_executer:
    ################################################################################### QUESTION 4
    #Quelles sont les parts de consommation de gaz et d'électricité représentées par chaque région en 2021 ?
    regions_gaz_elec=Pipeline([[Fenetrage,2021,1,2021,12,[4,9,10],True],[Grouper_somme,0],[Tri,1]]).applique()
    regions = Pipeline([[regions_gaz_elec],[Faire_liste,0]]).applique()
    conso_gaz = Pipeline([[regions_gaz_elec],[Faire_liste,1]]).applique()
    conso_elec  = Pipeline([[regions_gaz_elec],[Faire_liste,2]]).applique()
    plt.pie(conso_elec, labels = regions)
    plt.title("Part de la consommation d'électricité que représente chaque région")
    plt.show()
    plt.pie(conso_gaz, labels = regions)
    plt.title("Part de la consommation de gaz que représente chaque région")
    plt.show()

if 5 in questions_a_executer:
    ################################################################################### QUESTION 5
    # L'humidité a t elle un impact sur la consommation totale d'énergie en France? 

    conso_tot=Pipeline([[Fenetrage,2021,1,2021,12,[1,12],True],[Grouper_somme,0]]).applique() # Importe la table ELEC entre 01/2021 et 12/2021 en gardant les variables 
                                                                                                # Date et Conso brute totale.
                                                                                                # Groupe ensuite par date en sommant (aggrégation).

    humidite=Pipeline([[Fenetrage,2021,1,2021,12,[1,9],False],[Grouper_moyenne,0]]).applique()# Importe la table METEO entre 01/2021 et 12/2021 en gardant les variables 
                                                                                                # Date et humidite.
                                                                                                # Groupe ensuite par date en faisant la moyenne (aggrégation).

    Pipeline([[Jointure,humidite,conso_tot,0,0],[Tri,1],[Regression,1,3,"Consommation totale d'énergie en fonction de l'humidité en France"]]).applique() # Jointure des deux tables, tri croissant en fonction de la colonne humidite
                                                                                                                                                          # Puis tracé d'une régréssion linéaire avec X = humidite, Y = Conso totale
    
if 6 in questions_a_executer:
####################################  Exemple d'un autre moyen d'importer des données

    # Ici, on utilise un fichier meteo mais le code fonctionne avec nimporte quel csv.gz
    chemin1 = config.chemin_meteo
    nom1 = "synop.202203.csv.gz"
    # on commence par importer le fichier
    AutreTable1 = Import_csv(chemin1,nom1)
    # on peut ensuite le mettre en première position dans la Pipeline puis lui appliquer les fonctions que l'on souhaite
    # sans oublier de faire les conversions car celles ci ne sont plus automatiques pour les fichier quelconques.
    table=Pipeline([[AutreTable1],[Conversion_float,[7,9]],[Grouper_moyenne,1],[Tri,7],[Regression,7,9,"humidité en fonction de la température en Mars 2022"]]).applique()

    # Il est possible de faire de même en modifiant les chemins pour aller vers un fichier json quelconque et en faisant Import_json
    chemin2 = config.chemin_elec
    nom2 = "2022-12.json.gz"
    AutreTable2 = Import_json(chemin2,nom2)
    liste_des_regions = set(Pipeline([[AutreTable2],[Faire_liste,7]]).applique())
    print("la liste des régions est: "+str(liste_des_regions))

if 7 in questions_a_executer:
    ############################################# Dans cet exemple, on importe un fichier json avec la méthode généraliste (fonctionnant sur tout type de json)
    ############################################# puis on l'enregistre en tant que fichier csv sur le disque dur.

    ###    -----------> Il faut d'abord modifier le dossier d'enregistrement et le nom du fichier ligne 132.

    chemin3 = config.chemin_elec
    nom3 = "2022-12.json.gz"
    AutreTable3 = Import_json(chemin3,nom3)
    #Ecrire(AutreTable3,"C:/Users/Lucas LALOUE/Desktop/","nom_fichier").applique()
    