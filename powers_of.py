"""
DEFINE YOUR FUNCTIONS BELOW
"""


def print_powers_of():
    base = int(input("Please enter a positive integer to serve as the base: "))
    power = int(input("Please enter a positive integer to serve as the highest power: "))
    if base >= 0 and power >= 0:
        for x in range(0, power + 1, 1):
            result = base ** x
            print(str(base) + " ^ " + str(x) + " = " + str(result))
    else:
        print("ERROR: Both values must be POSITIVE INTEGERS.")


def print_even_powers_of_in_reverse():
    base = int(input("Please enter a positive integer to serve as the base: "))
    power = int(input("Please enter a positive integer to serve as the highest power: "))
    if power % 2 == 1:
        power -= 1
    if base >= 0 and power >= 0:
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
    Just some sample behavior.
    """
    print_powers_of()
    print_even_powers_of_in_reverse()

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
