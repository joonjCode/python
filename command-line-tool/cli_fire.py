import  fire
from getpass import getpass

def hello(name = 'world'):
	return f'hello {name}'

def login(name = None):
	if name == None:
		name = input('what is your name\n')
		pw = getpass('what is your password\n')

	return name, pw



if __name__ == '__main__':
	fire.Fire(hello)