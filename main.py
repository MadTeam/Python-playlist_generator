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


# <--------------------------------------------------------------------------------------------------------------------------------------------> #

'''Raccourcis:
(*1) Requête de génération finale à insérer

Exemples								Etat du code:

1) --genre rock 60 --genre hip-hop 30 --genre pop 10			=> (*1)
2) --genre rock 60 --genre hip-hop 30					=> Condition remplie (et correcte?) / (*1)
3) --genre rock 60 --genre hip-hop 30 --genre pop 10 --genre rap 20	=> Condition remplie (et correcte?) / (*1)

4) --genre rock 60 --genre hip-hop 30 --genre rap 110			=> Condition remplie (et correcte?) / (*1)
5) --genre rock 60 --genre hip-hop 30 --genre pop 40 --genre rap 110	=> Condition remplie (et correcte?) 
6) --genre rock 60 --genre hip-hop 30 --genre pop 10 --genre rap 110	=> Condition remplie (et correcte?) / (*1)'''

#Attributs supplémentaires
somme = 0. #Pour définir le total des elem[1] en un seul nombre
reste = 0. #Pour déterminer le nombre de pourcentage inutilisé lors d'une sélection
divid = 0. #Pour déterminer le pourcentage restant après la division de chaque elem[1] par le nombre d'elem[1] et leur addition (condition 3)
elmax = 0. #Pour définir les elem[1] dépassant 100 à 0 (none)
reatt = 0. #Pour déterminer le multiplicateur du pourcentage restant en fonction du total des elem[1] none (condition 4)
total = 0. #Pour définir à nouveau la somme avec le rajout du reste
none = 0.  #Pour rassembler tous les elem[1] none (conditions avec valeurs none)

#Dictionnaire d'arguments 
dict_args = dict()
for ARGS in ['genre', 'subgenre', 'artist', 'album', 'title']:
	if getattr(scan, ARGS) is not None:
		arg_list = getattr(scan, ARGS)
		dict_args[ARGS] = arg_list
		for elem in dict_args[ARGS]:
			elem[1] = functions.convert(elem[1], 1)
			print(dict_args)

#Genre est la concaténation du nom et du pourcentage
pourcentage = dict()
for ARGS in dict_args:
	pourcentage[ARGS] = dict_args
	for elem in dict_args[ARGS]:
		pourcentage[ARGS] = elem[1]
		#Chaque elem[1] d'un genre est compté dans l'attribut somme
		somme += elem[1]
		#print(somme)
		print(max(elem[1]))
		
#1) Condition fonctionnelle
#Dans le cas où la somme des elem[1] est égale à 100
if(somme == 100):
	log.debug(ARG+": \n\t-1: "+ str(elem[0]) +"\n\t-2: "+ str(elem[1])) #Affiche la valeur envoyée pour chaque argument
	#Générer directement la playlist
	print(somme)
	print('Condition n°1 remplie')

#Dans le cas où aucun elem[1] de la ligne ne dépasse pas 100
elif((max(elem[1])) < 100):
	while(somme != 100.):
		log.debug(ARG+": \n\t-1: "+ str(elem[0]) +"\n\t-2: "+ str(elem[1])) #Affiche la valeur envoyée pour chaque argument
	#2) Condition à tester
		if(somme < 100.):
		#Prendre elem[1] de chaque genre et les refactoriser pour obtenir un total de 100
			reste = 100. - somme
			#Acquérir le reste
			log.debug('Les valeurs ont été redéfinis pour permettre à l\'ensemble des pourcentages d\'atteindre 100%.')
			total = somme + (reste / len(elem[1]))
			#Générer la playlist
			print('Condition n°2 remplie')
	#3) Condition à tester
		'''elif(somme > 100.):
		#Prendre elem[1] de chaque genre et les refactoriser pour obtenir un total de 100
			if(somme >= 200.):
				log.warning('Le pourcentage total a dépassé de loin la valeur maximale autorisée')
				print('La somme des pourcentages égale ou excède les 200%. Le programme s\'est arrêté.')
			else:
				divid += elem[1] / len(elem[1])
				reste = 100. - divid
				reatt = reste / len(elem[1])
				total += elem[1] + reatt
				#Générer la playlist
				print('Condition n°3 remplie')'''
'''
#Dans le cas où un ou plusieurs elem[1] de la ligne dépassent 100
elif(max(elem[1])) > 100.:
	while(max(elem[1]) > 100.):
		elmax = max(elem[1]) 
		max(elem[1]) = 0.
		none = len(elem[1] = 0.)
	while(somme != 100.):
		log.debug(ARG+": \n\t-1: "+ str(elem[0]) +"\n\t-2: "+ str(elem[1])) #Affiche la valeur envoyée pour chaque argument
		elem[1] = functions.convert(elem[1], 1.) #Convertit l'argument 2 (pourcentage) en un décimal
		functions.chkValue(elem[1], 0., 101.) #Vérifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
	#4) Condition à tester
		if(somme < 100.):
		#Prendre les elem[1] none et leur attribuer équitablement le reste pour atteindre 100
			log.debug('Les valeurs none ont été redéfinis pour permettre à l\'ensemble des pourcentages d\'atteindre 100%.')
			reste = 100. - somme
			reatt = reste / none #Ici, reatt est le résultat de la division entre le reste et les elem[1] remis à zéro
			total = somme + (reatt * none) #Multiplie reatt par le nombre de none pour compléter la somme des elem[1] corrects
			#Générer la playlist
			print('Condition n°4 remplie')
	#5) Condition à tester
		elif(somme > 100.):
		#Arrêter le programme et afficher un message d'erreur
			log.warning('Somme maximale dépassée et pourcentage(s) individuel(s) dépassé(s)')
			print('Des genres dépassent le pourcentage maximal (100) et le total des genres restants le dépasse aussi.')
			print('Veuillez recommencer, s\'il vous plaît.')
			#Générer la playlist
			print('Condition n°5 remplie')
	#6) Condition à tester
		elif(somme == 100.):
		#Laisser à zéro les elem[1] et générer directement la playslist
			log.debug('Les valeurs none ont été délaissées pour permettre la génération de la playlist avec les valeurs correctes.')
			print('Condition n°6 remplie')
			
					
					
#Dans le cas où l'utilisateur est vraiment très con
elif(min(elem[1]) <= 0. or somme < 0.):
	log.warning('Valeur(s) saisie(s) négative(s) ou nulle(s)')
	print('Les pourcentages négatifs ne sont pas pris en compte par la ligne de commande. Le programme s\'est arrêté.')'''
