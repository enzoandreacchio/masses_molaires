def c_to_f(c):
	c = 1.8*c+32
	return c

def f_to_c(f):
	f = (f-32)/1.8
	return f

if __name__ == '__main__':
	c = input("c = ")
	c = int(c)
	print(c , "°C = " , c_to_f(c) , "°F")
