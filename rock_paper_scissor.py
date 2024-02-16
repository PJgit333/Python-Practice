computer_choice = "Scissors"
user_choice = input("Select an option: Rock, Paper or Scissor ")

if computer_choice == user_choice:
    print("its a tie")
elif user_choice == "Paper":
    print("Computer Wins")
elif user_choice == "Rock":
    print("User Wins")
else:
    print("Wrong selection")