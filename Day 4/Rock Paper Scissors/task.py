import random
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

game_image = [rock,paper,scissors]
user_choice = int(input('what do you choice \n choose 0 for rock \n choose 1 for paper \n choose 2 for scissors\n'))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])

comp_choice = random.randint(0,2)
print(comp_choice)

if user_choice >=3 or user_choice < 0:
    print("invalid command")
elif user_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and user_choice == 2:
    print("You lose!")
elif comp_choice > user_choice:
    print("You lose!")
elif user_choice > comp_choice:
    print("You win!")
elif comp_choice == user_choice:
    print("It's a draw!")