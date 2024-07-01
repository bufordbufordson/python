import time
from weird_number_generator import print_weird_numbers


def main():
    try:
        n = int(input("How many weird numbers would you like to generate? "))
        start_time = time.time()
        if n <= 0:
            print("The number must be positive")
            return

        print("The first", n, " weird numbers:")
        print_weird_numbers(n)
        elapsed = time.time() - start_time
        print("Found the first ", n, " weird numbers in ", elapsed, "seconds")
    except ValueError:
        print("That was not a valid integer.")

main()
