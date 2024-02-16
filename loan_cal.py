# get details of loan

money_owed = float(input("Money you owe, in dollars: "))
apr = float(input("Annual Percentage rate: "))
emi = float(input("EMI: "))
months = int(input("Number of months: "))

monthly_rate = apr/100/12

for i in range(months):
    #Interest to pay
    interest_paid = money_owed*monthly_rate

    # Add in interest
    money_owed = money_owed + interest_paid
    if (money_owed - emi < 0):
        print("Last payment is", money_owed)
        print("You paid off loan in", i+1,"months")
        break

    # Make payment
    money_owed = money_owed - emi

    print("Paid", emi, "of which", interest_paid, "was interest", end = " ")
    print("Remaining money: ", money_owed)