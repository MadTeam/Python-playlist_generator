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
log = logging('playlist.log', scan.verbose, fmt, datefmt)

for ARG in ['name', 'format', 'length']:
	elem = getattr(scan, ARG)
	if elem is not None:
		log.debug(ARG+" -> "+elem)

functions.init(log)
sql = functions.getSqlBdd('etudiant:passe', '172.16.99.2:5432', 'radio_libre')

##############################
# 'genre' est la concaténation du nom et du pourcentage
list_genre = list()
for ARGS in ['genre', 'subgenre', 'artist', 'album', 'title']:
	if getattr(scan, ARGS) is not None:
		arg_list = getattr(scan, ARGS)
		for elem in arg_list:
			if ARGS == 'genre':
				list_genre.append(functions.convert(elem[1], 666))

print(list_genre)

'''
for ARG in ['genre', 'subgenre', 'artist', 'album', 'title']:
	i = 0
	if getattr(scan, ARG) is not None:
		elem = getattr(scan, ARG)
		while i < len(elem):
			log.debug(ARG+" : \n\t-1 : "+str(elem[0])+"\n\t-2 : "+str(elem[1])) #affiche la valeur envoyee pour chaque argument
			elem[1] = functions.convert(elem[1], 666) #convertit l'argument 2 (pourcentage) en un entier
			functions.chkValue(elem[1], 0, 101) #verifie si la valeur absolue de l'argument 2 est compris entre 1 et 100

###########################'''
