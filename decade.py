# input returns a string value
age = int(input("How old are you? "))

decades = age/10
decades01 = age//10  #integer division

years = age%10

print("you are", int(decades), "decades old and", years, "old.")
print("You are " + str(decades01) + " decades old.")