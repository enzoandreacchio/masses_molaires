import random
import math

print("Bienvenue au jeu de la roulette")

while 1+1==2:
	mise = input("Misez un numéro compris entre 0 et 49 (inclus) : ")
	somme = input("Misez un montant en $ : ")
	try:
		mise = int(mise)
		somme = int(somme)
	except:
		print("Vous avez mal renseigné les montants...")
		continue

	if (0 <= mise <= 49) and (somme > 0):
		break
	else:
		print("Votre mise doit être comprise entre 0 et 49 (inclus) et votre montant doit être strictement positif...")
		continue


tirage = random.randrange(50)
print("Le numéro gagnant est : " , tirage , " !")

if tirage == mise:
	gain = 4*somme
elif (tirage%2==0 and mise%2==0) or (tirage%2==1 and mise%2==1):
	gain = math.ceil(1.5*somme)
else:
	gain = 0

print("Vous remportez donc : " , gain , "$.")