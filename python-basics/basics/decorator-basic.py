def my_decorator(func):
  def wrap_func(*args, **kwargs):
    print('*'*10)
    func(*args, **kwargs)
    print('*'*10)
  return wrap_func


@my_decorator
def hello(name, emoji = ':('):
  print(f'hello {name}', emoji)

@my_decorator
def bye():
  print('bye')

hello(name = 'niz')
bye()



# from time import time

# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1} ms')
#     return result
#   return wrapper


# @performance
# def long_time():
#   for i in range(100000):
#     i*5

# long_time()