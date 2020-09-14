from random import randint
import sys
# Generate a number 1 ~ 100
first_num = int(sys.argv[1])
second_num = int(sys.argv[2])
answer = randint(first_num,second_num)

# print(answer)
while True:
    try:
        # input from the user
        guess = int(input(f'Guess a number {first_num}-{second_num} : '))
        # Check if the number is the right guess.
        if first_num< guess < second_num:
            if guess > answer:
                print('Guess lower')
            elif guess < answer:
                print('Guess higher')
            elif guess == answer:
                print('Good job')
                break
        else:
            # Check if that input is between 1~100
            print(f'The number is not bwtn {first_num}-{second_num}')
    except ValueError as e:
        print('Please enter a number')
        continue
