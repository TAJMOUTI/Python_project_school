from random import randint
import time
print("\t\t\t\t\t*****MASTERMIND*****\n")
print("                                   Vous allez maintenant jouer au Mastermind.\n        Les regles du jeu sont tres simples: vous devez retrouver une combinaison de 4 chiffres tirées aleatoirement.\n        Pour ce faire, vous allez propserer 4 chiffres, trois possibilitées s'offrent alors à vous:\n\n               -votre chiffre est dans la combinaison à retrouver et il est bien placé\n\n               -votre chiffre est dans la combinaison à retrouver mais il est mal placé\n\n               -votre chiffre n'est pas dans la combinaison à retrouver\n\n                               A vous de jouer!\n\n")
mas1 = randint(0,9)
mas2 = randint(0,9)
mas3 = randint(0,9)
mas4= randint(0,9)
mastermind=[mas1,mas2,mas3,mas4]
compteur=1
t0= time.time ()

#print(mastermind)
for x in range(0,8):
	c1 = int(input("\nchiffre numero 1: "))
	c2 = int(input("\nchiffre numero 2: "))
	c3 = int(input("\nchiffre numero 3: "))
	c4 = int(input("\nchiffre numero 4: "))
	chiffres=[c1,c2,c3,c4]
	
	#print("Votre combinaison est : ",chiffre1,chiffre2,chiffre3,chiffre4\n)
	if(chiffres==mastermind):
		compteur==compteur+1
		print("\nVictoire!\n")
		print("\nVous avez deviné la combinaison en",compteur ,"coups\n")
		t1=time.time()
		
		total = print("temps:", str(t1-t0), "sec")
		break


	if(c1==mas1) :
		print(c1,"est bien placé\n")
	elif(c1 in mastermind):
		print(c1,"est dans la liste mais est mal placé\n")
	else: 
		print(c1,"n'est pas dans la liste\n")
	if(c2==mas2) :
		print(c2,"est bien placé\n")
	elif(c2 in mastermind):
		print(c2,"est dans la liste mais est mal placé\n")
	else: 
		print(c2,"n'est pas dans la liste\n")

	if(c3==mas3) :
		print(c3,"est bien placé\n")
	elif(c3 in mastermind):
		print(c3,"est dans la liste mais est mal placé\n")
	else: 
		print(c3,"n'est pas dans la liste\n")

	if(c4==mas4) :
		print(c4,"est bien placé\n")
	elif(c4 in mastermind):
		print(c4,"est dans la liste mais est mal placé\n")
	else: 
		print(c4,"n'est pas dans la liste\n")
	
	if(chiffres==mastermind):
		print("Vous avez gagné !\n")
		break





