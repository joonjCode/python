import pprint



req = [
    'windwos-cursess;sys_platform=="win32"',
    'pytest==5.2',
    'pytest-cov',
    'pre-commit',
]

'''
oldway
if '==' in s:
    pkg = s.split('==', 1)[0]
if ';' in s:
    s = s.split(';', 1)[0]
return s
'''
def sort_key(s:str)-> str:
    s,_,_ = s.partition('==')
    s,_,_ = s.partition(';')
    

    return s
    

def main () -> int:
    pprint.pprint(sorted(req))
    return 0

if __name__ =='__main__':
    exit(main())
