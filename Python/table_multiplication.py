def tab(nb, max):
	i=1
	while i <= max:
		print(i , " x " , nb , " = " , i*nb)
		i += 1

print("Ce programme permet d'obtenir la table de multiplication d'un naturel n par les naturels de 1 à i")
a = input("n = ")
a = int(a)
b = input("i = ")
b = int(b)
tab(a, b)
