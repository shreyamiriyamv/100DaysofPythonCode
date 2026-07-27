from art import logo
print (logo)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
random_number = random.randint(0,2)
game_images = [rock, paper, scissors]

if number >= 0 and number <= 2:
    print(game_images[number])
    print ("Computer chose: ")
    print (game_images[random_number])

    if ((number == 0 and random_number == 2) or
            (number == 1 and random_number == 0) or
                (number == 2 and random_number == 1)):
        print("You win!")
    elif (number == random_number):
        print("It's a draw!")
    else:
        print("You lose!")

else:
    print("You typed an invalid number, you lose!")