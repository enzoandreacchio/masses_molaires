from scipy.integrate import quad
import numpy as np
import math




#//////////////////////////////////////// FONCTION CLE /////////////////////////////////////////////////
def f(x):
	return (math.sin(math.cos(x**2)))
#///////////////////////////////////////////////////////////////////////////////////////////////////////





msg_code = input("Entrez le message à décoder : ")
liste_coeffs = msg_code.split("e")

def g(x):
	r = 0
	for i in range(0, len(liste_coeffs)):
		r += float(liste_coeffs[i]) * x ** (len(liste_coeffs) - 1 - i)
	return r

def h(x):
	return (math.copysign(f(x)-g(x), 1))

print(h(5))
print(quad(h, 0, 1)[0])
for i in range(1, len(liste_coeffs) + 1):
	print(quad(h, i-1, i)[0])

