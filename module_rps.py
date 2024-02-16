import random as r

computer_choice = r.choice(['rock','paper','scissor'])
user_choice = input("Select an option: Rock, Paper or Scissor ")

if computer_choice == user_choice:
    print("It's a tie")
elif user_choice == 'rock' and computer_choice == 'scissor':
    print("You won")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You won")
elif user_choice == 'paper' and computer_choice == 'scissor':
    print("You lost")
elif user_choice == 'scissor' and computer_choice == 'paper':
    print("You won")
