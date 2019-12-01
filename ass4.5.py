import random

num = random.randint(1,30)


i = 0


while i != 3:
    
    guess = int(input('guess the correct number = '))
    if num == guess:
        print('bingo')
    elif guess<num:
        print('oops! your guess is less than the correct')
    elif guess>num:
        print('oops! your guess is greater than the correct')
    i = i+ 1

print('correct answer is ' + str(num))