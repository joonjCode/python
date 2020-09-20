import requests
import hashlib
import sys
# sha1 gen : https://passwordsgenerator.net/sha1-hash-generator/



def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    res.raise_for_status()
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, c in hashes:
        # print('h',h)
        if h == hash_to_check:
            return c
    return 0

def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(first5_char, tail)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... change the password')
        else:
            print(f'{password} was not found. Safe to use')
    return 'done'



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
