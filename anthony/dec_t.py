import functools

def dec(func):
	@functools.wraps(func)
	def dec_inner(*args, **kwargs):
		print(f'got {args} {kwargs}')
		ret = func(*args, **kwargs)
		print('after')
		return ret
	return dec_inner

def dec2(greeting, farewell):
	def dec2_decorator(func):
		@functools.wraps(func)
		def dec2_inner(*args, **kwargs):
			print(greeting)
			ret = func(*args, **kwargs)
			print(farewell)
			return ret
		return dec2_inner
	return dec2_decorator


@dec2('hello', 'goodbye')
def f(x:int) -> None:
	print(f'hello {x}')


def main():
	breakpoint()
	f(1)

if __name__ == '__main__':
	exit(main())
