from fonctions_celcius_fahrenheit import *
print("Si vous voulez convertir des degrés celcius en fahrenheit tapez 1")
print("Si vous voulez convertir des degrés fahrenheit en celcius tapez 2")
k = input("Choix : ")
if k == '1':
	c = input("c = ")
	c = int(c)
	print(c , "°C = " , c_to_f(c) , "°F")
elif k == '2':
	f = input("f = ")
	f = int(f)
	print(f , "°F = " , f_to_c(f) , "°C")
else:
	print("Mauvaise commande...")

