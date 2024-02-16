expenses = [10.50, 8, 5, 15, 29, 5, 3]

sum01 = 0

for x in expenses:
    sum01 = sum01 + x

print("You spent $", sum01, sep = '')

print("Sum using sum func", sum(expenses))