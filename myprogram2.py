""" uses not n % i instead of n % i == 0 to optimize myprogram.py """
semiperfects = set(); primes = []

def main(): 
    x = 2; weirds = []; n = 30000
    while n > 0:
        if isweird(x) == 1: weirds.append(x); n = n - 1
        x = x + 1
    print("First", len(weirds), "weird nos:\n", weirds)

def isweird(n): 
    global primes; global semiperfects; primedivs = []; a = n
    for i in primes:
        while not a % i: primedivs.append(i); a = a//i 
        if i * i > a: break
    if a > 1:
        primedivs.append(a)
        if a == n: primes.append(n); return 0 
    sum_fctrs = 1; divs = set(primedivs) 
    for i in divs: sum_fctrs = sum_fctrs*(i**(primedivs.count(i)+1)-1)//(i-1)
    df = sum_fctrs - 2 * n
    if df <= 0: 
        if df == 0: semiperfects.add(n)
        return 0
    divs = [1]; last_prime = 0; fctr = 0; slice_len = 0
    for prime in primedivs:
        if last_prime != prime: slice_len = len(divs); fctr = prime
        else: fctr *= prime
        for i in range(slice_len):
            div = divs[i] * fctr
            if div not in semiperfects: divs.append(div)
            else: return 0 
        last_prime = prime
    x = 1; divs.pop(-1); divs = {i for i in divs if i <= df}
    target = n - (df + n - sum(divs))
    if target < 0: return 1
    for d in divs: x |= x << d
    if x >> target & 1: semiperfects.add(n); isweird = 0
    else: isweird = 1
    return isweird 
    
main()
