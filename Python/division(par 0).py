def f(a,b):
	try:
		e = a/b
	except:
		print("Il y  a un problème avec les données")
	else:
		print(a , " / " , b , " = " , e)

print("Dans ce programme, on va tester des divisions")
a = input("a = ")
a = int(a)
b = input("b = ")
b = int(b)
f(a,b)
