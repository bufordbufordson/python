semiperfects = set();
primes = []


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


def print_weird_numbers(n):
    x = 2
    while n > 0:
        if isweird(x) == 1:
            end = "\n" if n % 20 == 0 else " "
            print(x, end=end)
            n = n - 1
        x = x + 1
    print("\ndone.")


def isweird(n):
    global primes;
    global semiperfects;
    primedivs = [];
    a = n
    for i in primes:
        while a % i == 0: primedivs.append(i); a = a // i
        if i * i > a: break
    if a > 1:
        primedivs.append(a)
        if a == n: primes.append(n); return 0
    sum_fctrs = 1;
    divs = set(primedivs)
    for i in divs: sum_fctrs = sum_fctrs * (i ** (primedivs.count(i) + 1) - 1) // (i - 1)
    df = sum_fctrs - 2 * n
    if df <= 0:
        if df == 0: semiperfects.add(n)
        return 0
    divs = [1];
    last_prime = 0;
    fctr = 0;
    slice_len = 0
    for prime in primedivs:
        if last_prime != prime:
            slice_len = len(divs);
            fctr = prime
        else:
            fctr *= prime
        for i in range(slice_len):
            div = divs[i] * fctr
            if div not in semiperfects:
                divs.append(div)
            else:
                return 0
        last_prime = prime
    x = 1;
    divs.pop(-1);
    divs = {i for i in divs if i <= df}
    target = n - (df + n - sum(divs))
    if target < 0: return 1
    for d in divs: x |= x << d
    if x >> target & 1:
        semiperfects.add(n);
        isweird = 0
    else:
        isweird = 1
    return isweird


main()
