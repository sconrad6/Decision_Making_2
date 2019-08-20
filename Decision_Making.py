cont = "y"
while cont == "y":

    def user_input():
        return int(input("Please enter a number between 1 and 100"))

    number = user_input()
    while number < 1 or number > 100:
        print("Invalid number")
        user_input()
        break


    def display_number_message():
        if number % 2 != 0:
            return "odd"
        elif number % 2 == 0 and number < 25:
            return "Even and less than 25"
        elif number % 2 == 0 and number > 26:
            return "even"
        elif number % 2 != 0 and number >= 60:
            return "odd"

    print(display_number_message())

    cont = input("Would you like to continue? Y/N").lower()


print("Goodbye!")





