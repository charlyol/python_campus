from statistics import mean
from random import shuffle


def main():
    # Creat a variable to store the user's name
    # username = input("Entrez votre nom: ")
    username = "Max"
    print("Hello World ! " + username)
    # Creat a variable to store the user's age
    # age = input("Entrez votre age: ")
    age = 26
    # Creat a variable to store the user's wallet money
    # wallet = input("Entrez votre porte-monnaie: ")
    wallet = 100
    is_happy = True
    # Print the user's age and wallet money
    print("Vous avez " + str(age) + " ans et " + str(wallet) + " euros dans votre porte-monnaie.")
    age += 10
    print("Vous avez " + str(age) + " ans et " + str(wallet) + " euros dans votre porte-monnaie.")
    # print("Hello World!")
    # print("This is the first page of the project.")
    # Creat a variable to store the first note
    note1 = input("Entrez votre premiere note: ")
    # Creat a variable to store the second note
    note2 = input("Entrez votre deuxieme note: ")
    # Creat a variable to store the third note
    note3 = input("Entrez votre troisieme note: ")
    # Creat a variable to store the average of the three notes
    result = (int(note1) + int(note2) + int(note3)) / 3
    # Print the average of the three notes
    print("Votre moyenne est de " + str(result))


def main2():
    wallet = 5000
    computer_price = 1200

    # the computer price is less than 1000€
    if wallet >= computer_price > 1000:
        print("You can buy the computer")
        wallet -= computer_price
        print("You have {}€ now in your wallet".format(wallet))
    else:
        print("You can't buy the computer, you have only {}€ in your wallet".format(wallet))

    text = ("You can't buy the computer", "You can buy the computer")[computer_price <= 1000]
    print(text)


def main3():
    password = input("Enter your password: ")
    password_length = len(password)
    if password_length <= 8:
        print("Your password is too short")
    elif 8 < password_length <= 12:
        print("Your password is medium")
    else:
        print("Your password is long enough")


def main4():
    # creat a short list of online players
    online_players = ["Max", "Charles", "Fernando", "Pierre", "Alex"]
    # display the list of online players
    print(online_players)
    # display the first and last player of the list
    print(online_players[0])
    # display the last player of the list
    print(online_players[len(online_players) - 1])
    # display the first player of the list and change it
    online_players[0] = "Maxou"
    print(online_players)
    # add a player to the list
    online_players.insert(2, "Lando")
    print(online_players)
    # add a player to the end of the list
    online_players.append(["Oscar", 'Max'])
    print(online_players)
    # remove a player from the list
    online_players.remove(["Oscar", 'Max'])
    print(online_players)
    # clear the list of online players
    online_players.clear()
    print(online_players)


def main5():
    notes = [8, 12, 10,
             18, 20, 14,
             ]
    print(notes)
    print(notes[0])
    #modul : statistics mean
    result = mean(notes)
    print("la moyenne de l'élève est de {}".format(result))
    # modul : random shuffle
    shuffle(notes)
    print(notes)


def main6():
    #for split method input string
    text = input('Entrer une chain de caractère de la forme (email pseudo password):').split(' ')
    print(text)
    # for loop to display the elements of the list with index
    print("Salut {}, votre email est {} et votre mot de passe est {}".format(text[1], text[0], text[2]))


def main7():
    print("vous êtes le client N°1")
    # loop for : for each client
    for num_client in range(1, 6):
        # 6 is not included
        print("vous êtes le client N°{}".format(num_client))
    emails = ['test@gmail.com', 'max@gmail.com', 'contact@gmail.com', 'redbull@gmail.com']
    # blacklist
    blacklist = ['contact@gmail.com', 'test@gmail.com']
    # loop foreach : for each email
    for toto in emails:
        if toto in blacklist:
            print("email {} est dans la blacklist".format(toto))
        else:
            print("email envoyé à {}".format(toto))
    # loop while : while is true
    salary = 1500
    #while salary is less than 2000€, +120€
    while salary < 2000:
        salary += 120
        print("votre salaire est de {}€".format(salary))
    print("end of program")
    # YouTuber max have 2500 subscribers
    subscribers_count = 2500
    # he gains 10% of subscribers each month
    month = 0
    #how many subscribers will he have after 24 months
    while month <= 24:
        #augmentation of 10% of subscribers per month
        subscribers_count *= 1.1
        #display the number of subscribers
        print("you have {:.0f} subscribers".format(subscribers_count))
        # next month
        month += 1
    print("end of program")

    def main8():
        value = 123.456789

        # Use the method format()
        print("Using format():")
        print("Value with 2 decimal places: {:.2f}".format(value))
        print("Value with 4 decimal places: {:.4f}".format(value))
        print("Value with no decimal places: {:.0f}".format(value))

        # Use the f-strings
        print("\nUsing f-strings:")
        print(f"Value with 2 decimal places: {value:.2f}")
        print(f"Value with 4 decimal places: {value:.4f}")
        print(f"Value with no decimal places: {value:.0f}")

        # Use operator %
        print("\nUsing % operator:")
        print("Value with 2 decimal places: %.2f" % value)
        print("Value with 4 decimal places: %.4f" % value)
        print("Value with no decimal places: %.0f" % value)


def welcome_message():
    print("Welcome to the program")
    result = 5 + 6
    print("The result is : {:.0f} ".format(result))


def main9():
    welcome_message()
    print("End of the program")


def next_year(year):
    print("End of the year {} ".format(year))
    year += 1
    print("Welcome to the new year {} ".format(year))


def main10():
    year = 2018
    next_year(year)
    next_year(year + 1)


def addition():
    result = 5 + 5
    return result


def multiply():
    result = 5 * 8
    return result


def addition_n(n):
    result = 5 + n
    return result


def main11():
    print("Result of the addition : {:.0f}".format(addition()))
    print("Result of the multiplication : {:.0f}".format(multiply()))
    print("Result of the addition : {:.0f}".format(addition_n(5)))
    print("Result of the addition : {:.0f}".format(addition_n(4)))
    print("Result of the addition : {:.0f}".format(addition_n(9)))


#creat a function max() to return the maximum of two numbers
def max_of_two_numbers(a, b):
    if a > b:
        return a
    else:
        return b


def main12():
    first_value = int(input("Enter the first value: "))
    second_value = int(input("Enter the second value: "))
    max_value = max_of_two_numbers(first_value, second_value)
    print("The maximum value between {} and {} is {}".format(first_value, second_value, max_value))


# recursive function
def add(a):
    a += 1
    print(a)
    # limit the number of recursive calls
    if a < 10:
        add(a)


def main13():
    add(2)


if __name__ == '__main__':
    # main()
    # main2()
    # main3()
    # main4()
    # main5()
    # main6()
    # main7()
    # main8()
    # main9()
    # main10()
    # main11()
    # main12()
    main13()
