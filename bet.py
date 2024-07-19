#This is just project with fake money i am making is as it is a fun game there is no betting intention
#stay away from these things
import random as rd
import sys

def askUser():
    global bet
    global user
    user = int(input(f'Enter number in list {number} :'))
    bet = int(input(f'Whats your bet balance = {money} :'))

def game():

    global money
    global number
    money = 1000000
    number = [1,2,3,4,5,6,7,8,9,10]
    comp = rd.choice(number)
    askUser()
    if user in number:
        if user == comp:
            print('You Win !!')
            money = money + bet
        else:
            print('You lose better luck next time. :(')
            money = money - bet
        print(f'\t amount : {money} \n number = {comp}') 
    else:
        print('Enter a Valid number')
        askUser()
    ask = input('Do you want to continue (y/n): ').lower()
    if ask == 'y':
        game()
    elif ask == 'n':
        sys.exit()
    else:
        game()

game()