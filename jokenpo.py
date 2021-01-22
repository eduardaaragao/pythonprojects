from random import randint
from time import sleep

# Author: Maria Eduarda
# Description: This is a program that simulates Rock, Paper and Scissors game. Hope you like it!
print('''Your options:

[0] Rock
[1] Paper
[2] Scissors''')

myChoice = int(input('What is your choice? '))
items = ('Rock', 'Paper', 'Scissors')

if myChoice != 0 and myChoice != 1 and myChoice != 2:
    print('Choice not accepted')
else:
    print('Thinking...')
    sleep(2)
    computerChoice = randint(0, 2)

    if computerChoice == myChoice:
        print('Tie!! Computer also chose', items[computerChoice])
    else:
        if myChoice == 0 and computerChoice == 1:
            print('Computer won!')
        if myChoice == 0 and computerChoice == 2:
            print('You won!')
        if myChoice == 1 and computerChoice == 2:
            print('Computer won!')
        if myChoice == 1 and computerChoice == 0:
            print('You won!')
        if myChoice == 2 and computerChoice == 1:
            print('You won!')
        if myChoice == 2 and computerChoice == 0:
            print('Computer won!')
        print('Computer chose {} and you chose' .format(items[computerChoice]), items[myChoice])
