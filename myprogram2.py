from time import time
start = time()

from ordered_set import OrderedSet

primitivesp_nos = set(); primes = OrderedSet([])

def main(): 
    x = 2; weird_nos = []; n = 10000
    while n > 0:
        if isweird(x) == 1: weird_nos.append(x); n = n - 1
        x = x + 1        
    print("First", len(weird_nos), "weird nos:\n", weird_nos)

def isweird(n): 
    global primes; global primitivesp_nos; pr_fctrs = []; a = n
    for i in primes:
        b = a 
        while a % i == 0: pr_fctrs.append(i); a = a//i
        if i * i > a: break
        if b != a:
            if a in primes: pr_fctrs.append(a); a = 1; break
    if a > 1: pr_fctrs.append(a)
    if a == n: primes.add(n); return 0 
    sum_fctrs = 1; divisors = set(pr_fctrs) 
    for i in divisors: sum_fctrs = sum_fctrs*(i**(pr_fctrs.count(i)+1)-1)//(i-1)
    difference = sum_fctrs - 2 * n
    if difference <= 0: 
        if difference == 0: primitivesp_nos.add(n)
        return 0
    # Code from Jerome Richard: stackoverflow.com/questions/6800193
    divisors = [1]; last_prime = 0; fctr = 0; slice_len = 0
    for prime in pr_fctrs:
        if last_prime != prime: slice_len = len(divisors); fctr = prime
        else: fctr *= prime
        for i in range(slice_len):
            d = divisors[i] * fctr
            if d not in primitivesp_nos: divisors.append(d)
            else: return 0 
        last_prime = prime
    x = 1; divisors = set(i for i in divisors if i <= difference)
    ns = n - (difference + n - sum(divisors))
    if ns < 0: return 1
    for d in divisors: x |= x << d
    if x >> ns & 1: primitivesp_nos.add(n); return 0
    else: return 1 
    
main()

end = time() 
print("Execution time: ", round(end - start, 2), "s")
