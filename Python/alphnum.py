import unicodedata

ch = input("\n\n\nLa chaîne de caractère à étudier est : ")
r = "Cette chaîne mesure " + str(len(ch)) + " caractères."
print(r)
ch = unicodedata.normalize('NFKD', ch).encode('ascii', 'ignore')
ch = str(ch)
ch = ch[:len(ch)-1]
ch = ch[2:]


i=0
abc = "abcdefghijklmnopqrstuvwxyz"
pr = str()
while i < int(len(ch)):
	lettre = ch[i]
	lettre = lettre.lower()
	if lettre == " ":
		print(" ")
		if i != 0:
			pr = pr[:len(pr)-1]
		pr = str(pr) + "   "
		i+=1
		continue

	j=0
	while (lettre != abc[j]):
		j+=1
	j+=1
	print(lettre , ":" , j)
	pr = str(pr) + str(j) + "."
	i+=1

pr = pr[:len(pr)-1]
print("\n Le message codé est : \n" , pr)