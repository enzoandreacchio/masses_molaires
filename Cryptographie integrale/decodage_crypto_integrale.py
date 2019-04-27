from scipy.integrate import quad
import numpy as np
import math


#//////////////////////////////////////// FONCTION CLE /////////////////////////////////////////////////
def f(x):
    return (math.sin(math.cos(x**2)))
#///////////////////////////////////////////////////////////////////////////////////////////////////////

"""
# Définition de la fonction qui permet de calculer l'intégrale par parties d'une fonction f sur un intervalle [a;b]
def integ(f, a, b):
    output = 0
    inf = 0
    sup = 0
    sec = (b - a) / 100000
    i = a
    while i <= b:
        inf += f(i) * sec
        i += sec
        sup += f(i) * sec
    return (inf + sup) / 2
"""

# Input du message à décoder
msg_code = input("Entrez le message à décoder : ")

# Création d'une liste contenant tous les coefficients du polynôme transmis
liste_coeffs = msg_code.split("e")


# Création de la fonction polynômiale transmise
def g(x):
    r = 0
    for i in range(0, len(liste_coeffs)):
        r += float(liste_coeffs[i]) * x ** (len(liste_coeffs) - 1 - i)
    return r


# Création de la fonction qui sera intégrée pour donner l'aire entre les deux courbes
def h(x):
    return (f(x) - g(x))

# Output des valeurs obtenues
for i in range(1, len(liste_coeffs) + 1):
    # Valeur calculée grâce à la fonction de spicy.integrate
    print(abs(quad(h, i - 1, i)[0]))
