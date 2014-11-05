'''Raccourcis:

(*1) Requête de génération finale à insérer
(*2) Adapter à la liste pourcent_list

Exemples								Etat du code:

1) --genre rock 60 --genre hip-hop 30 --genre pop 10			=> (*1) / (*2)
2) --genre rock 60 --genre hip-hop 30					=> Condition remplie / (*1) / (*2)
3) --genre rock 60 --genre hip-hop 30 --genre pop 10 --genre rap 20	=> Condition à insérer / (*1) / (*2)

4) --genre rock 60 --genre hip-hop 30 --genre rap 110			=> Condition à compléter / (*1) / (*2)
5) --genre rock 60 --genre hip-hop 30 --genre pop 40 --genre rap 110	=> Condition remplie
6) --genre rock 60 --genre hip-hop 30 --genre pop 10 --genre rap 110	=> Condition à compléter / (*1) / (*2)
'''
#Attributs supplémentaires
reste float
total float

#1)
#Dans le cas où la somme des elem[1] est égale à 100
if('''somme('''elem[1]''')''') == 100):
#Générer directement la playlist
	


#Dans le cas où aucun elem[1] de la ligne ne dépasse pas 100
elif(max(elem[1])) < 100):
	while (i < len(elem[1]):
		log.debug(ARG+" : \n\t-1 : "+str(elem[0])+"\n\t-2 : "+str(elem[1])) #Affiche la valeur envoyée pour chaque argument
		elem[1] = functions.convert(elem[1], 1.) #Convertit l'argument 2 (pourcentage) en un decimal
		functions.chkValue(elem[1], 0, 101) #Vérifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
	#2)
		if(len(elem[1]) < 100):
		#Prendre elem[1] de chaque genre et les refactoriser pour obtenir un total de 100
			reste = 100. - len(elem[1])
			#Acquérir le reste
				total = '''somme('''elem[1]''')''' + (reste / len(elem[1]))
			

	#3)
		if(len(elem[1]) > 100):
		#Prendre elem[1] de chaque genre et les refactoriser pour obtenir un total de 100
			


#Dans le cas où un ou plusieurs elem[1] de la ligne dépassent 100
elif(max(elem[1])) > 100):
	elem[1] = 0 #Ligne à revoir
	while (i < len(elem[1]):
		log.debug(ARG+" : \n\t-1 : "+str(elem[0])+"\n\t-2 : "+str(elem[1])) #Affiche la valeur envoyée pour chaque argument
		elem[1] = functions.convert(elem[1], 1) #Convertit l'argument 2 (pourcentage) en un entier
		functions.chkValue(elem[1], 0, 101) #Vérifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
	#4)
		if('''somme('''elem[1]''')''' < 100):
		#Prendre les elem[1] dépassant 100 et leur attribuer équitablement le reste pour atteindre 100
			reste = 100 - len(elem[1])
			for(elem[1] == 0):
			#Acquérir le reste (à retravailler)
				total = elem[1] + reste

	#5)
		if('''somme('''elem[1]''')''' > 100):
		#Arrêter le programme et afficher un message d'erreur
			log.warning('Somme maximale dépassée et pourcentage(s) individuel(s) dépassé(s)')
			print('Des genres dépassent le pourcentage maximal (100) et le total des genres restants le dépasse aussi.')
			print('Veuillez recommencer, s\'il vous plaît.')
			

	#6)
		if('''somme('''elem[1]''')''' == 100):
		#Générer un message de validation
			print('Les genres dépassant les 100% ont été mis à 0%. Souhaitez-vous tout de même valider votre sélection?')
				if(scan = str('non')):
				#Si non, réafficher la sélection et laisser l'utilisateur redéfinir les pourcentages
					
				else:
				#Si oui, générer directement la playlist
					

	
