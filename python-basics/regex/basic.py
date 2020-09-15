import re

pattern = re.compile('this')

s = 'this is a test text for regex'
# search(), finall(), fullmatch(), .match()
a = pattern.search('this')
print(a.group())
# https://regex101.com/
