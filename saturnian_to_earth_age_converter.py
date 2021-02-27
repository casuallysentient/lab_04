"""
DEFINE YOUR FUNCTIONS BELOW
"""


def print_earth_age():
    """
    Takes an age on Saturn and converts it into an age on Earth, divided into years, months, and days.

    pre-condition: The function needs a positive age of a Saturnian.

    post-condition: The function has taken that age and converted it to its equivalent age on Earth. Alternatively, if a negative number was entered, an error message will be printed.
    """
    saturn_age = float(input("How old is the Saturnian you are talking to? "))
    if saturn_age >= 0:
        earth_age = int(saturn_age * 10759)
        years_on_earth = earth_age // 365
        earth_age -= (years_on_earth * 365)
        months_on_earth = earth_age // 30
        earth_age -= (months_on_earth * 30)
        print("This Saturnian is " + str(years_on_earth) + " Earth-years, " + str(months_on_earth) + " Earth-months, and " + str(earth_age) + " Earth-days old.")
    else:
        print("You can't be younger than 0. Sounds like someone's lying to me.")


"""
DEFINE YOUR FUNCTIONS ABOVE
"""


def main():
    """
    Executes print_earth_age().

    pre-condition: Nothing has yet been executed.

    post-condition: print_earth_age() has been executed.
    """
    print_earth_age()

# DO NOT WRITE CODE BEYOND THIS LINE ###


if __name__ == '__main__':
    main()
