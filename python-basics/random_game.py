from random import randint
import sys
def get_random_number():
    first_num = int(sys.argv[1])
    second_num = int(sys.argv[2])
    answer = randint(first_num,second_num)
    return first_num, second_num, answer
# print(get_random_number())

def play_game(first_num:int, second_num:int, answer:int):
    count: int = 0
    while True:
        try:
            # input from the user
            guess = int(input(f'Guess a number {first_num}-{second_num} : '))
            # Check if the number is the right guess.
            if first_num<= guess <= second_num:
                if guess > answer:
                    print('Guess lower')
                    count += 1
                elif guess < answer:
                    print('Guess higher')
                    count +=1
                elif guess == answer:
                    print(f'Good job you got it in {count} tries')
                    break
            else:
                # Check if that input is between 1~100
                print(f'The number is not bwtn {first_num}-{second_num}')
        except ValueError as e:
            print('Please enter a number')
            continue

f,s,a = get_random_number()
play_game(f,s,a)
