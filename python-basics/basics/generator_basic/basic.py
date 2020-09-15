# Generators : iterable

def generator_func(num):
	for i in range(num):
		yield i*2

# g = generator_func(100)
# print(g) # object
# print(next(g)) # 0
# print(next(g)) # 2 4 6




for item in generator_func(100):
	print(item)


def make_list(num):
	result = []
	for i in range(num):
		result.append(i*2)
	return result
