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
			#coeff[i][j].append(-coo[j+1][0])
			#coeff[i][j].append(0)
			#continue

		for k in range(1, j+1):

			if key == 1:
				value = coeff[i][j-1][k] + (coeff[i][j-1][k-1] * -coo[j+1][0])
			else:
				value = coeff[i][j-1][k] + (coeff[i][j-1][k-1] * -coo[j][0])


			print(coeff)

			coeff[i][j].append(value)
			if j == k:
				coeff[i][j].append(0)


	#a = []
	#a = coeff[i][choix-1]

	#for l in range(0, choix):
	#	del coeff[i][l]

	#coeff[i] = a
	#del coeff[i][choix]

	print(coeff)




#print(coo)
#print(coeffs_poly_l)
#print(coeff)




#{1: (3, 4), 2: (2, 1), 3: (5, 6)}