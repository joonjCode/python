#  Built-in : https://docs.python.org/3/library/exceptions.html

while True:
	try:
		age = int(input('what is your age?'))
		# print(age)
		10/age
		raise ValueError('Value aint right')
	except ZeroDivisionError:
		print('0000')
	else:
		print('done!')
		break
	finally:
		print('ok I am finally done')