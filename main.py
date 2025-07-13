# Rock paper scissor game

''' Rock wins against Scissors
    Scissors wins against Paper
    Paper wins against Rock '''

'''
    0 for Rock
    1 for Paper
    2 for Scissors
                      '''

import random
import time
cc=pc=0
n=0

while n != 5:

    Rock='''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
       '''

    Paper='''
           _______
      ---'    _____)
               ______)
              _______)
             _______)
      ---._________)
       '''

    Scissors='''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
      '''
    print()
    print('0 for Rock\n1 for Paper\n2 for Scissors')

    a=int(input('Enter your choice (0,1,2): '))

    print()

    b=random.randint(0,2)

    if a == 0 and b == 1:
        print(f"You choose {Rock} \nCPU choose {Paper}\n")
        print('You Lose')
        cc+=1

    elif a==0 and b==2:
        print(f"You choose {Rock} \nCPU choose {Scissors}\n")
        print('You won')
        pc += 1

    elif a==1 and b==0:
        print(f"You choose {Paper} \nCPU choose {Rock}\n")
        print('You won')
        pc += 1

    elif a==1 and b==2:
        print(f"You choose {Paper} \nCPU choose {Scissors}\n")
        print('You Lose')
        cc += 1

    elif a==2 and b==0:
        print(f"You choose {Scissors} \nCPU choose {Rock}\n")
        print('You Lose')
        cc += 1

    elif a==2 and b==1:
        print(f"You choose {Scissors} \nCPU choose {Paper}\n")
        print('You won')
        pc += 1

    elif a == b:
        print("It's a Draw.")
        print()

    else:
        print('Wrong Choice!!!!!!!')
        print()

    if pc > cc:
        n=pc

    else:
        n=cc

else:
    if pc == 5:
        print()
        print('**** Congratulations You won the game ****')
    else:
        print()
        print('**** You loose the game ****')

print()
print('Thanks you for playing the game.')

print()
print('Game developer Tejvir Chauhan.')
time.sleep(5)
