import re
pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

string = 'nizzz'

# a = pattern.search(string)
# print(a)


'''
At least 8 char
contain any letters, numbers and etc
end with number
'''

#([A-Za-z0-9$%#@]{7,}[0-9])
