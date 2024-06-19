
def suma_normal(a,b):
	return a+b

def producto_normal(a,b):
	return a*b

def suma_general(*args):

	total = 0
	for i in args:
		total +=i

	print(total)
	return total


def producto_general(*args):
	
	total = 0
	for i in args:
		total +=i

	print(total)

	return total

