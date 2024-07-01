import time
from weird_number_finder import is_weird


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


def print_weird_numbers(n):
    candidate = 2
    while n > 0:
        if is_weird(candidate) == 1:
            end = "\n" if n % 20 == 0 else " "
            print(candidate, end=end)
            n = n - 1
        candidate = candidate + 1
    print("\ndone.")


main()
