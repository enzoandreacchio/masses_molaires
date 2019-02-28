from decimal import Decimal

coo = {}
x = ""
y = ""
ask_x = ""
ask_y = ""
coeff_p = float()
coeffs_poly_l = {}
coeff = {}
coeffs_npl = {} #coefficients des numémrateurs des polynômes de Lagrange


#------------------------------------INPUT DU NOMBRE DE POINTS-------------------------------------------

print("\n\n\nProgramme permettant de trouver le polynôme qui passe par n points du plan : ")
while 1+1==2:
	choix = input("Nombre de points à relier : ")
	try:
		choix = int(choix)
		break
	except:
		print("Mauvais choix ! ")
		continue

#-------------------------------INPUT ET ENREGISTREMENT DES COORDONNEES----------------------------------

for i in range(1, choix+1):
	while 1+1==2:
		print("Coordonnées du point " , i , " : ")
		ask_x = "x_" + str(i) + " = "
		ask_y = "y_" + str(i) + " = "
		x = input(ask_x)
		y = input(ask_y)
		try:
			x = int(x)
			y = int(y)
			break
		except:
			print("Une coordonnée doit être un nombre...\n")
			continue
	coo[i] = (x,y)

#---------------------------CALCUL DES COEFFS DVT LES POLYNOMES DE LAGRANGE----------------------------

for i in range(1, choix+1):
	d=1
	for j in range(1, choix+1):
		if j==i:
			continue
		d *= coo[i][0]-coo[j][0]
	coeff_p = (coo[i][1])/d
	coeffs_poly_l[i] = coeff_p
	
#-----------------CALCUL DES COEFFS DE CHAQUE NUMERATEUR DE CHAQUE POLYNOME DE LAGRANGE----------------

for i in range(1, choix+1):
	key = 0
	value = 0

	coeff[i] = {}
	coeff[i][0] = [1, 0]
		
	for j in range(1, choix):

		coeff[i][j] = [1]

		if j == i:
			key = 1

		for k in range(1, j+1):

			if key == 1:
				value = coeff[i][j-1][k] + (coeff[i][j-1][k-1] * -coo[j+1][0])
			else:
				value = coeff[i][j-1][k] + (coeff[i][j-1][k-1] * -coo[j][0])


			coeff[i][j].append(value)
			if j == k:
				coeff[i][j].append(0)


	a = []
	a = coeff[i][choix-1]

	for l in range(0, choix):
		del coeff[i][l]

	coeff[i] = a
	del coeff[i][choix]

#----------------------------------CALCUL DES COEFFS FINAUX----------------------------------------

coeff['total'] = {}

for i in range(1, choix+1):
	for j in range(0, choix):
		coeff[i][j] *= coeffs_poly_l[i]
		if i == 1:
			coeff['total'][j+1] = 0
		coeff['total'][j+1] += coeff[i][j]


for l in range(1, choix+1):
	del coeff[l]

#----------------------------------ARRONDISSEMENT DES COEFFS--------------------------------------

for i in range(1, choix+1):
	a = ""
	part_ent = ""
	part_dec = ""
	coeff['total'][i] = str(coeff['total'][i])
	a = coeff['total'][i]

	a = a.split(".")

	part_ent = a[0]
	part_dec = a[1]

	part_dec = a[1][:100]
	
	a = part_ent + "." + part_dec
	coeff['total'][i] = a

#--------------------------------------AFFICHAGE DES RESULTATS-----------------------------------

output = ""
for i in range(1, choix):
	output += str(coeff['total'][i]) + "x^" + str(choix-i) + " + "
output += str(coeff['total'][choix])

print("\n\n")
print(output)