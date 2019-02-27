a = input("Saisis une année : ")
b = False
a = int(a)

if a%4 == 0 and a%100 != 0:
	b = True
elif a == 400:
	b = True
else:
	b = False

if b:
	print("L'année ", a, " est bissextile.")
else:
	print("L'année ", a, " n'est pas bissextile.")
