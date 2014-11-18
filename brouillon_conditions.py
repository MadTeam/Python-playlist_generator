'''Raccourcis:
(*1) Requête de génération finale à insérer

Exemples								Etat du code:

1) --genre rock 60 --genre hip-hop 30 --genre pop 10			=> (*1)
2) --genre rock 60 --genre hip-hop 30					=> Condition remplie (et correcte?) / (*1)
3) --genre rock 60 --genre hip-hop 30 --genre pop 10 --genre rap 20	=> Condition remplie (et correcte?) / (*1)

4) --genre rock 60 --genre hip-hop 30 --genre rap 110			=> Condition remplie (et correcte?) / (*1)
5) --genre rock 60 --genre hip-hop 30 --genre pop 40 --genre rap 110	=> Condition remplie (et correcte?) 
6) --genre rock 60 --genre hip-hop 30 --genre pop 10 --genre rap 110	=> Condition à compléter (et correcte?) / (*1)'''

#Attributs supplémentaires
somme float #Pour définir le total des elem[1] en un seul nombre
reste float #Pour déterminer le nombre de pourcentage inutilisé lors d'une sélection
divid float #Pour déterminer le pourcentage restant après la division de chaque elem[1] par le nombre d'elem[1] et leur addition (condition 3)
reatt float #Pour déterminer le multiplicateur du pourcentage restant en fonction du total des elem[1] none (condition 4)
total float #Pour définir à nouveau la somme avec le rajout du reste
valid bool  #Pour valider une boucle (condition 6)
none int    #Pour rassembler tous les elem[1] none (conditions 4, 5, 6)

#Chaque elem[1] d'un genre est compté dans l'attribut somme
somme += elem[1]

#1)
#Dans le cas où la somme des elem[1] est égale à 100
if(somme == 100):
#Générer directement la playlist
	

#Dans le cas où aucun elem[1] de la ligne ne dépasse pas 100
elif(max(elem[1])) < 100):
	while(!somme == 100):
		log.debug(ARG+": \n\t-1: "+ str(elem[0]) +"\n\t-2: "+ str(elem[1])) #Affiche la valeur envoyée pour chaque argument
		elem[1] = functions.convert(elem[1], 1.) #Convertit l'argument 2 (pourcentage) en un décimal
		functions.chkValue(elem[1], 0, 101) #Vérifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
	#2)
		if(somme < 100):
		#Prendre elem[1] de chaque genre et les refactoriser pour obtenir un total de 100
			reste = 100 - somme
			#Acquérir le reste
			log.debug('Les valeurs ont été redéfinis pour permettre à l\'ensemble des pourcentages d\'atteindre 100%.')
			total = somme + (reste / len(elem[1]))
	#3)
		elif(somme > 100):
		#Prendre elem[1] de chaque genre et les refactoriser pour obtenir un total de 100
			if(somme >= 200):
				log.warning('Le pourcentage total a dépassé de loin la valeur maximale autorisée')
				print('La somme des pourcentages égale ou excède les 200%. Le programme s\'est arrêté.')
			else:
				divid += elem[1] / len(elem[1])
				reste = 100 - divid
				reatt = reste / len(elem[1])
				total += elem[1] + reatt

#Dans le cas où un ou plusieurs elem[1] de la ligne dépassent 100
elif(max(elem[1])) > 100):
	while(!max(elem[1] > 100)):
		max(elem[1]) = 0
		none = len(elem[1] = 0)
	while(!somme == 100):
		log.debug(ARG+": \n\t-1: "+ str(elem[0]) +"\n\t-2: "+ str(elem[1])) #Affiche la valeur envoyée pour chaque argument
		elem[1] = functions.convert(elem[1], 1) #Convertit l'argument 2 (pourcentage) en un entier
		functions.chkValue(elem[1], 0, 101) #Vérifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
	#4)
		if(somme < 100):
		#Prendre les elem[1] none et leur attribuer équitablement le reste pour atteindre 100
			log.debug('Les valeurs none ont été redéfinis pour permettre à l\'ensemble des pourcentages d\'atteindre 100%.')
			reste = 100 - somme
			reatt = reste / none #Ici, reatt est le résultat de la division entre le reste et les elem[1] remis à zéro
			total = somme + (reatt * none) #On multiplie reatt par le nombre de none pour compléter la somme des elem[1] corrects
	#5)
		elif(somme > 100):
		#Arrêter le programme et afficher un message d'erreur
			log.warning('Somme maximale dépassée et pourcentage(s) individuel(s) dépassé(s)')
			print('Des genres dépassent le pourcentage maximal (100) et le total des genres restants le dépasse aussi.')
			print('Veuillez recommencer, s\'il vous plaît.')
	#6)
		elif(somme == 100):
		#Générer un message de validation
			while(!valid = true):
				print('Les genres dépassant les 100% ont été mis à 0%. Souhaitez-vous tout de même valider votre sélection (o/n)?')
				if(scan = str('n')):
				#Si non, réafficher la sélection et laisser l'utilisateur redéfinir les pourcentages
					
					valid = true
				elif(scan = str('o')):
				#Si oui, générer directement la playlist
						
					valid = true
				else:
				#La réponse est autre que 'o' ou 'n'
					valid = false
				
#Dans le cas où l'utilisateur est vraiment très con
elif(min(elem[1]) <= 0 || somme < 0):
	log.warning('Valeur(s) saisie(s) négative(s) ou nulle(s)')
	print('Les pourcentages négatifs ne sont pas pris en compte par la ligne de commande. Le programme s\'est arrêté.')
