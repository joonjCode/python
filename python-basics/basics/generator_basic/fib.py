def fib(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a 
		a = b
		b = temp + b 


def fib2(number):
	a = 0
	b = 1
	arr = []
	for i in range(number):
		arr.append(a)
		temp = a 
		a = b
		b = temp + b 
	return arr

for x in fib2(100):
	print(x)
