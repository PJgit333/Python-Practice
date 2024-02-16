current_movies = {'The Grinch': '11:00am',
                 'Rudolph': '1:00pm',
                 'Frosty the Snowman':'3:00pm',
                 'Cars':'5:00pm'}


print("We are showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like th showtime for? \n")

showtime=current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie,"is at", showtime)