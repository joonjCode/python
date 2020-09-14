from time import time
def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f'took {t2-t1} s')
		return result
	return wrapper


@performance
def long_time():
	print('1')
	for i in range(10000):
		i*5

@performance
def long_time2():
	print('2')
	for i in list(range(10000)):
		i*5

# long_time()
# long_time2()

class MyGen():
	current = 0
	def __init__(self, first, last):
		self.first= first
		self.last = last
	
	def __iter__(self):
		return self

	def __next__(self):
		if MyGen.current < self.last:
			num = MyGen.current
			MyGen.current += 1
			return num
		raise StopIteration

gen = MyGen(0,100)
for i in gen:
	print(i)