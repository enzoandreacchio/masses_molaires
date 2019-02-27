def afficher(*texte):
	texte = str(texte)
	tab = texte.split(' ')
	i=0
	texte = tab[i]
	while i < (len(tab)-1):
		i+=1
		texte = str(texte) + " " + tab[i]
	return texte

a = input("Texte : ")
print(afficher(a))