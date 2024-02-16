total = 0
expenses = []

num = int(input("Enter the number of expenses: "))

for i in range(num):
    expenses.append(float(input("Enter your expense: ")))

total = sum(expenses)

print("You spent $", total, sep='')