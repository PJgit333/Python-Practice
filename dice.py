import random as r

def roll_dice():
    a = r.randint(1,6)
    b = r.randint(1,6)
    dice_total = a + b
    print("dice1:", a, "dice2:", b) 
    return dice_total

def main():
    player1 = input("Enter player1 name:\n")
    player2 = input("Enter player2 name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "rolled", roll1)
    print(player2, "rolled", roll2)

    if roll1 > roll2 :
        print(player1,"wins")
    elif roll2 > roll1:
        print(player2,"wins")
    else:
        print("tie hogaya bhai!")

main()