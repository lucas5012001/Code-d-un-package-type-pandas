##################################################### FICHIER DE CONFIGURATION #####################################################################




###################################### Configurations à modifier lorsqu'on change de PC pour faire fonctionner le dossier main.py

chemin_meteo = "C:/Users/Lucas LALOUE/Desktop/projet/data/meteo/" #--# Chemin vers les tables meteo
chemin_elec = "C:/Users/Lucas LALOUE/Desktop/projet/data/elec/" #--# Chemin vers les tables elec
chemin_fichier_regions_stations = "C:/Users/Lucas LALOUE/Desktop/projet/data/" #--# Chemin vers le fichier postesSynopAvecRegions.csv
   
   



#Inutile de modifier les paramètres suivants :
###################################### Le programme est utilisable avec d'autres données sans changer
                                     # ces paramètres. Leur changement permet uniquement d'automatiser
                                     # des conversions de colonnes ou d'ajouter des options au code pour
                                     # le faire évoluer si on souhaite utiliser durablement de nouvelles données.
                                     # Regarder les classes Import_csv, Import_json et le fichier README pour
                                     # plus de détails.


###################### CONFIG CSV - ELECTRICITE
col_int_meteo = [2,3,4,5,9,11,12,13,15,16,17,18,19,20,21,22,23,29,34,46,47,48,49,50,51,52,53,54,55,56,57] 
col_float_meteo = [6,7,8,10,14,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45] 
mq_csv = 'mq' #Renseigner la forme des valeurs manquantes dans le fichier csv pour adapter le fichier json.
index_stations = 0

###################### CONFIG JSON - METEO
colonnes_elec = ['date_heure','date','heure','code_insee_region','region',
'consommation_brute_gaz_grtgaz','statut_grtgaz','consommation_brute_gaz_terega','statut_terega',
'consommation_brute_gaz_totale','consommation_brute_electricite_rte','statut_rte','consommation_brute_totale']
fields_name_elec = 'fields'       # Nom de la clé du dictionnaire contenant les champs
col_int_elec = [3,5,7,9,10,12] 
col_float_elec = []
index_regions = 4
