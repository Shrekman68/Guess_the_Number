# import random for generate random number
import random

# taking lower and upper bound from user
# checking if lower is greater than upper
# taking input until lower is smaller than upper
# using while loop
while True:
    lower = int(input('Enter lower bound: '))
    upper = int(input('Enter upper bound: '))
    if lower > upper:
        print('Please input valid lower and upper bound: ')
    else:
        break
# generate random number between lower and upper
random_num = random.randint(lower, upper)
# asking user for guess the number
# until user guess it correct
# by showing the message
# if user guess too low or too high
# or out of limit bound
while True:
    user_input = int(input(f'Great, now guess a number between {lower} and {upper}: '))
    # if user_input is out of range limit bound
    if user_input < lower or user_input > upper:
        print('Please guess number in limit')
    # if user guess correct print message
    # and break
    # if user guess greater than number
    elif user_input > random_num:
        print('Try again! you guess too high')
    # if user guess smaller than number
    elif user_input < random_num:
        print('Try again! you guess too low')
    elif user_input == random_num:
        print('You got it!')
        break
        