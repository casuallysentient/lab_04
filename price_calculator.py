"""
DEFINE YOUR FUNCTIONS BELOW
"""

def get_final_price():
    """
    Takes a list of prices and calculates what the final price of the purchase will be.

    pre-condition: The function needs the subtotal of the order (the total of all the prices entered added together) to be greater than or equal to 1000.

    post-condition: The function has added the numbers together, applied a sales tax of 8%, and, if there were more than 10 items, applied a 20% post-tax discount. It will print the final price (and alert you to your discount, if you were eligible for it).
    """
    subtotal = 0
    num_items = 0
    while subtotal < 1000:
        item_price = float(input("Enter the price of your item: "))
        subtotal += item_price
        num_items += 1
    final_cost = subtotal + (0.08 * subtotal)
    if num_items > 10:
        print("20% discount applied!")
        final_cost = final_cost - (0.2 * final_cost)
    print("The total price is " + str(final_cost) + ".")

"""
DEFINE YOUR FUNCTIONS ABOVE
"""


def main():
    """
    Executes print_earth_age().

    pre-condition: Nothing has yet been executed.

    post-condition: print_earth_age() has been executed.
    """
    get_final_price()

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
