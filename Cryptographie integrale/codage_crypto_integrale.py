from scipy.integrate import quad
import numpy as np


def txt_to_nb(txt):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	liste = []
	txt = str(txt)
	for i in range(1, len(txt) + 1):
		for j in range(1, 27):
			if txt[i-1:i] == alphabet[j-1:j]:
				liste.append(j)
	return liste




#//////////////////////////////////// FONCTION PROVISOIRE ///////////////////////////////////////////////
def f(x):
	return (3*x**2 - 4*x + 2)
#///////////////////////////////////////////////////////////////////////////////////////////////////////


# Requête du message à coder à l'utilisateur
message = input("Message à coder : ")
# Transformation du message texte en une liste de nombres correspondants
message = txt_to_nb(message)

# Création de la matrice B de l'équation AX = B où X est la matrice inconnue
mat_B = np.eye(len(message), 1)
for i in range(0, len(message)):
	mat_B[i] = message[i] + quad(f, i, i+1)[0]


# Pour un message de taille n, on considère un polynôme de degré n - 1 (donc avec n coefficients)
nb_coeffs_f = len(message)

# Ainsi, il existe un unique polynôme de degré n - 1 qui correspondent aux n points (que l'on va ensuite transmettre)



# Création du dictionnaire contenant les n - 1 listes des n coefficients de la fonction polynômiale "f"
coeffs = {}
for i in range(1, len(message) + 1):
	coeffs[i] = []
	for j in range(1, nb_coeffs_f + 1):
		coeffs[i].append(0)

# Remplissage des listes avec les coefficients correspondants
for i in range(1, len(message) + 1):
	for j in range(1, nb_coeffs_f + 1):
		coeffs[i][nb_coeffs_f - j] = (i**j - (i-1)**j)/j

# Création de la matrice A (qui devrait être inversible...)
mat_A = np.eye(len(message), nb_coeffs_f)

# Remplissage de la matrice A
for i in range(1, len(message) + 1):
	mat_A[i-1] = coeffs[i]

# Inversion de la matrice A
inv_mat_A = np.linalg.inv(mat_A)

# Réalisation du prpduit matriciel entre A et B pour obtenir la matrice inconnue X
mat_X = inv_mat_A.dot(mat_B)


# Création du polynôme à transmettre à l'utilisateur 2
output = ""
for i in range(0, len(message)):
	mat_X[i][0] = float(mat_X[i][0])
	if i == len(message) - 1:
		output += str(mat_X[i][0])
	elif i == len(message) - 2:
		output += str(mat_X[i][0]) + " * x + "
	else:
		output += str(mat_X[i][0]) + " * x^" + str(len(message) - (i+1)) + " + "

print("Le polynôme à transmettre est : ")
print(output)
