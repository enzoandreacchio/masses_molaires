coo = {}
x = ""
y = ""
ask_x = ""
ask_y = ""
coeff_p = float()
coeffs_poly_l = {}
coeff = {}
coeffs_npl = {} #coefficients des numémrateurs des polynômes de Lagrange
test = {}
frac = {}
frac_f = {}




#---------------------------------------IMPORTATION DES VALEURS-----------------------------------

a = ""
with open("file.txt", "r") as file:
	a = file.read()
	a = a.split(".")

for i in range(1, 119):
	coo[i] = (i, int(a[i-1]))

choix = 118

#---------------------------CALCUL DES COEFFS DVT LES POLYNOMES DE LAGRANGE----------------------------

for i in range(1, choix+1):
	d=1
	for j in range(1, choix+1):
		if j==i:
			continue
		d *= coo[i][0]-coo[j][0]
	coeff_p = (coo[i][1])/d
	coeffs_poly_l[i] = coeff_p
	test[i] = d



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


for i in range(1, choix+1):
	for j in range(0, choix):
		coeff[i][j] *= coo[i][1]


for i in range(1, choix+1):
	frac[i] = {}
	for j in range(0, choix):
		frac[i][j+1] = [coeff[i][j], test[i]]


def somme_frac(frac_1, frac_2):
    num_1 = frac_1[0] * frac_2[1]
    num_2 = frac_2[0] * frac_1[1]
    deno_commun = frac_1[1] * frac_2[1]
    num = num_1 + num_2
    return [num, deno_commun]

frac_f = {}
for i in range(1, choix+1):
	for j in range(1, choix):
		frac[j+1][i] = somme_frac(frac[j][i], frac[j+1][i])
	frac_f[i] = frac[choix][i]


def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

def simp(f):
	d = pgcd(f[0], f[1])
	f[0] /= d
	f[1] /= d
	frac = [f[0], f[1]]
	return frac

for i in range(1, choix+1):
	frac_f[i] = simp(frac_f[i])
	for j in range(0, 2):
		frac_f[i][j] = int(frac_f[i][j])


output = ""
for i in range(1, choix-1):
	if frac_f[i][1] == 1:
		output += str(frac_f[i][0]) + ".x^(" + str(choix-i) + ") + "
	else:
		output += "(" + str(frac_f[i][0]) + " / " + str(frac_f[i][1]) + ").x^(" + str(choix-i) + ") + "

if frac_f[choix-1][1] == 1:
	output += str(frac_f[choix-1][0]) + ".x + "
else:
	output += "(" + str(frac_f[choix-1][0]) + " / " + str(frac_f[choix-1][1]) + ").x + "

if frac_f[choix][1] == 1:
	output += str(frac_f[choix][0])
else:
	output += str(frac_f[choix][0]) + " / " + str(frac_f[choix][1])

print("\n\n\n")
print("Le polynôme passant par ces points est : ")
print(output)

"""
with open("output.txt", "w") as file:
	file.write(output)"""
