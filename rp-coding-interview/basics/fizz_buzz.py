'''
1. Replace all inte that are evenly divisible by 3 with '
fizz'
2. Replace all int divisble by 5 with 'buzz
3. replace all int div by both 3 and 5 with fizzbuzzz
numbesrs = [45,22, 14, 65, 97, 72]

output = 
'''

def fizz_buzz(num):
    # for i in range(len(num)):
    #     if i % 3 == 0:
    #         num[i]  = 'fizz'
    #     if i % 5 == 0 :
    #         num[i] = 'buzz'
    #     if i %3 ==0 and i%5==0:
    #         num[i] = 'fizzbuzz'

    # return num

    for idx, val in enumerate(num):
        if val % 3==0:
            num[idx] = 'fizz'
        if val % 5 ==0:
            num[idx] = 'buzz'
        if val%3==0 and val%5 ==0:
            num[idx] = 'fizzbuzz' 

    return num

num = [45,22, 14, 65, 97, 72]
print(fizz_buzz(num))