
def find_acronym():
    look_up = input("What acronym would you like to look up?\n")

    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return 

    if not found:
        print("The acronym doesn't exist!")

def add_acronym():
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition?\n")
    # r for reading
    # w for write (overwrites the previous file)
    # a for append
    with open('acronyms.txt', 'a') as file:
        file.write(acronym+' - '+definition+'\n')

def main():
    # ask the user whether they want to find or add an acronym

    choice = input("Want to (A)dd or (F)ind acronym: ")
    if choice == "A":
        add_acronym()
    elif choice == "F":
        find_acronym()
    else:
        print("Wrong choice")
        main()

main()