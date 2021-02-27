"""
DEFINE YOUR FUNCTIONS BELOW
"""


def print_batch_amount():
    """
    Takes a list of amounts of each ingredient and calculates how much mochi you can make with it.

    pre-condition: Four positive integers must be entered for the values of each of the four ingredients in grams.

    post-condition: The function has converted the amounts from grams to cups and calculated how many times you can take 3 cups of mochiko, 1.5 cups of sugar, 2 cups of cornstarch, and 1 cup of anko before you run out. This number is displayed as the number of batches of mochi you can make.
    """
    mochiko = float(input("Enter an amount (g) of mochiko: ")) / 220
    sugar = float(input("Enter an amount (g) of sugar: ")) / 220
    cornstarch = float(input("Enter an amount (g) of cornstarch: ")) / 220
    anko = float(input("Enter an amount (g) of anko: ")) / 220
    mochi = 0
    if mochiko >= 0 and sugar >= 0 and cornstarch >= 0 and anko >= 0:
        while mochiko >= 3 and sugar >= 1.5 and cornstarch >= 2 and anko >= 1:
            mochi += 1
            mochiko -= 3
            sugar -= 1.5
            cornstarch -= 2
            anko -= 1
        print("With this amount of ingredients, you can make " + str(mochi) + " batch(es) of 24 mochi.")
    else:
        print("All values must be positive.")


"""
DEFINE YOUR FUNCTIONS ABOVE
"""


def main():
    """
    Executes print_batch_amount().

    pre-condition: Nothing has yet been executed.

    post-condition: print_batch_amount() has been executed.
    """
    print_batch_amount()

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
