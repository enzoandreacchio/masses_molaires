import math
def prime(n,p):
	if (max(n,p))%(min(n,p))==0:
		return False
	else:
		return True

print("Grâce à ce programme, vous pourrez tester la primalité entre deux entiers n et p")
n = input("n = ")
n = int(n)
p = input("p = ")
p = int(p)

r = prime(n,p)
if r:
	print(n , " et " , p , " sont premiers entre eux.")
else:
	print(n , " et " , p , " ne sont pas permiers entre eux.")
	