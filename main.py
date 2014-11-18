#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''importation des bibliotheques nécessaires'''
from config import *

'''argparse'''
parser = argparse()
scan = parser.parse_args() #la variable 'scan' conservera l'ensemble des arguments

'''logging'''
fmt = "%(levelname)s %(asctime)s : %(message)s"
datefmt="%d/%m/%Y - %H:%M:%S"
log = logging('playlist.log', scan.verbeux, fmt, datefmt)

for ARG in ['nom', 'format', 'temps']:
	elem = getattr(scan, ARG)
	if elem is not None:
		log.debug(ARG+" -> "+elem)

functions.init(log)
scan.temps = functions.convert(scan.temps, 666)
#configuration de base
##############################
dict_args = dict()

for ARGS in ['genre', 'sousgenre', 'artiste', 'album', 'titre']:
	if getattr(scan, ARGS) is not None:
		arg_list = getattr(scan, ARGS)
		dict_args[ARGS] = arg_list
		for elem in dict_args[ARGS]:
			elem[1] = functions.convert(elem[1], 666)

log.debug(dict_args)

pourcentage = dict()
for ARGS in dict_args:
	pourcentage[ARGS] = dict_args
	for elem in dict_args[ARGS]:
		pourcentage[ARGS] = elem[1]

log.debug(pourcentage)
#récupération des arguments et factorisation des pourcentages
##################################
where = str()
i = 0

for ARGS in dict_args:
	for elem in dict_args[ARGS]:
		if i == 1:
			if scan.intersection:
				where += " AND " + ARGS + " ~ '"+ elem[0] +"'"
			else:
				where += " OR " + ARGS + " ~ '"+ elem[0] +"'"
		else:
			where += ARGS + " ~ '"+ elem[0] +"'"
			i = 1


log.debug("conditions SQL(regex compris) : "+where)
sql = functions.getSqlBdd('etudiant:passe', '172.16.99.2:5432', 'radio_libre', where)

for elem in sql:
	log.info(elem)
#récupération de la liste des musiques exigées
###################################

















#génération de la playlist
###############################
