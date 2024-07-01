from typing import Set, List


def print_weird_numbers(n):
    candidate = 2
    while n > 0:
        if is_weird(candidate) == 1:
            end = "\n" if n % 20 == 0 else " "
            print(candidate, end=end)
            n = n - 1
        candidate = candidate + 1
    print("\ndone.")


semi_perfects: Set[int] = set()
primes: List[int] = []


def is_weird(x):
    prime_divisors = get_prime_divisors(x)

    sum_factors = 1
    divs = set(prime_divisors)
    for i in divs:
        sum_factors = sum_factors * (i ** (prime_divisors.count(i) + 1) - 1) // (i - 1)
    df = sum_factors - 2 * x
    if df <= 0:
        if df == 0:
            semi_perfects.add(x)
        return 0
    divs = [1]
    last_prime = 0
    fctr = 0
    slice_len = 0
    for prime in prime_divisors:
        if last_prime != prime:
            slice_len = len(divs)
            fctr = prime
        else:
            fctr *= prime
        for i in range(slice_len):
            div = divs[i] * fctr
            if div not in semi_perfects:
                divs.append(div)
            else:
                return 0
        last_prime = prime
    x = 1
    divs.pop(-1)
    divs = {i for i in divs if i <= df}
    target = x - (df + x - sum(divs))
    if target < 0: return 1
    for d in divs: x |= x << d
    if x >> target & 1:
        semi_perfects.add(x)
        isweird = 0
    else:
        isweird = 1
    return isweird


def get_prime_divisors(x: int) -> List[int]:
    prime_divisors = []
    a = x
    for i in primes:
        while a % i == 0:
            prime_divisors.append(i)
            a //= i
        if i * i > a:
            break
    if a > 1:
        prime_divisors.append(a)
        if a == x:
            primes.append(x)
    return prime_divisors
