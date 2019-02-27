import random

size = input("Taille de l'échantillon : ")
size = int(size)
a = str()
tab = []
i=0
while i < size:
	tab.append(random.randrange(11))
	i+=1

i=0
nb = tab[i]
while i < len(tab)-1:
	i+=1
	nb += tab[i]
nb = nb/(len(tab))
print(nb)