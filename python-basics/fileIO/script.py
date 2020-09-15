
#  r+, w ,a

try:
    with open('app.txt', 'r') as f:
        print(f.readlines())
except FileNotFoundError as e:
    print('file does not exists')
    raise e
except IOError as e:
    print('IO error')
    raise e
