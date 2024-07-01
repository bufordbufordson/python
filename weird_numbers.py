from weird_number_generator import print_weird_numbers


def main():
    try:
        n = int(input("How many weird numbers would you like to generate? "))
        if n <= 0:
            print("The number must be positive")
            return

        print("The first", n, "weird numbers:")
        print_weird_numbers(n)
    except ValueError:
        print("That was not a valid integer.")

main()
