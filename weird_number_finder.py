from typing import Set, List


semi_perfects: Set[int] = set()
primes: List[int] = []


def is_weird(x):
    prime_divisors = get_prime_divisors(x, primes)

    sum_factors = calculate_sum_of_factors(prime_divisors)
    df = sum_factors - 2 * x

    if df < 0:
        return 0
    if df == 0:
        semi_perfects.add(x)

    divisors = [1]
    last_prime = 0
    factor = 0
    slice_len = 0
    for prime in prime_divisors:
        if last_prime != prime:
            slice_len = len(divisors)
            factor = prime
        else:
            factor *= prime
        for i in range(slice_len):
            div = divisors[i] * factor
            if div not in semi_perfects:
                divisors.append(div)
            else:
                return 0
        last_prime = prime

    num = 1
    divisors.pop()
    divisors = { i for i in divisors if i <= df }
    target = num - (df + num - sum(divisors))

    if target < 0:
        return 1

    for divisor in divisors:
        num |= num << divisor

    if num >> target & 1:
        semi_perfects.add(x)
        isweird = 0
    else:
        isweird = 1

    return isweird


def get_prime_divisors(x: int, primes: List[int]) -> List[int]:
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


def calculate_sum_of_factors(prime_divisors: List[int]) -> int:
    divs = set(prime_divisors)
    sum_factors = 1
    for i in divs:
        sum_factors = sum_factors * (i ** (prime_divisors.count(i) + 1) - 1) // (i - 1)
    return sum_factors
