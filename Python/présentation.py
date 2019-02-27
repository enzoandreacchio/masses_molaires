nom = input("Nom : ")
prenom = input("Prénom : ")
age = input("Age : ")

presentation = "Vous vous appelez {0} {1} et vous avez {2} ans".format(nom, prenom, age)
print(presentation)
choix = input("C'est bien ça ? (O/N)")
if choix.lower() == "o":
	print("Génial !")
elif choix.lower() == "n":
	print("Dommage...")
else:
	print("Il y a un problème avec le choix !")