# <, <=, ==, >=, >, !=

temperature = 90

forecast = "rainy"

'''if temperature > 80:
    print("AHhhh, that's hot.")
    print("Stay inside.")
elif temperature < 60:
    print("It's cold outside!")
else:
    print("Move out")
'''

'''if temperature > 80 or temperature < 60:
    print("Stay inside")
else:
    print("Move out now!")
'''

if temperature < 80 and forecast != "rainy":
    print("Go Outside!")
else:
    print("Stay inside!")
