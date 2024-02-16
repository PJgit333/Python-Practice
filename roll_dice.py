import random as r

roll = r.randint(1,6)



guess = int(input("Enter your guess: "))

if guess == roll:
    print("You guessed it right")
else:
    print("Try again")

print("Computer rolled "+ str(roll))