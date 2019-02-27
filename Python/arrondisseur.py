def arrondir(nb_float, nb_dec):
	nb_float = str(nb_float)
	nb_float = nb_float.split(".")
	part_ent = nb_float[0]
	part_dec = nb_float[1][:nb_dec]
	nb_arrondi = str(part_ent) + "," + str(part_dec)
	return nb_arrondi



dividende = input("Dividende : ")
diviseur = input("Diviseur : ")
dividende = int(dividende)
diviseur = int(diviseur)

a = dividende / diviseur
print("Résultat en float : " , a)
i = input("Nombre de chiffres après la virgule : ")
i = int(i)

print("Résultat arrondi à {0} chiffres après la virgule : {1}".format(i, arrondir(a, i)))



#a = str(a)
#a = a.split(".")
#dec = a[1][:i]
#ent = a[0]
#nb = str(ent) + "," + str(dec)
#print("Résultat arrondi à {0} chiffres après la virgule : {1}".format(i, nb))



