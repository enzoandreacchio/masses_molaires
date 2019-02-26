liste_z = ''
liste_masses = ''
masse_entree = ''
inp = ''

with open("file.txt", "w") as file:
	for i in range(1, 118):
		liste_z += str(i) + "."
		inp = str(i) + " -> " 
		masse_entree = input(inp)
		liste_masses += masse_entree + "."

	file.write(liste_masses)


	





