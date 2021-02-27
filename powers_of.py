"""
DEFINE YOUR FUNCTIONS BELOW
"""


def print_powers_of():
    """
    Takes a base and a power and incrementally prints the result of the base to each integer power between 0 and the power entered.

    pre-condition: Two positive integers must be entered.

    post-condition: The program has incrementally printed the result of the base to each integer power between 0 and the power entered. If a negative integer was entered, an error message is displayed.
    """
    base = int(input("Please enter a positive integer to serve as the base: "))
    power = int(input("Please enter a positive integer to serve as the highest power: "))
    if base >= 0 and power >= 0:
        for x in range(0, power + 1, 1):
            result = base ** x
            print(str(base) + " ^ " + str(x) + " = " + str(result))
    else:
        print("ERROR: Both values must be POSITIVE INTEGERS.")


def print_even_powers_of_in_reverse():
    """
    Takes a base and a power and incrementally prints the result of the base to each even integer power in reverse between the power entered and 0.

    pre-condition: Two positive integers must be entered.

    post-condition: The program has incrementally printed the result of the base to each even integer power in reverse between the power entered and 0. If a negative integer was entered, an error message is displayed.
    """
    base = int(input("Please enter a positive integer to serve as the base: "))
    power = int(input("Please enter a positive integer to serve as the highest power: "))
    if base >= 0 and power >= 0:
        if power % 2 == 1:
            power -= 1
        for x in range(power, -1, -2):
            if x >= 0:
                result = base ** x
                print(str(base) + " ^ " + str(x) + " = " + str(result))
    else:
        print("ERROR: Both values must be POSITIVE INTEGERS.")


"""
DEFINE YOUR FUNCTIONS ABOVE
"""


def main():
    """
    Executes print_powers_of() and print_even_powers_of_in_reverse().

    pre-condition: Nothing has yet been executed.

    post-condition: print_powers_of() and print_even_powers_of_in_reverse() have been executed.
    """
    print_powers_of()
    print_even_powers_of_in_reverse()

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
