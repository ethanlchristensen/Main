def countPrimes(n):
    primes = [True]*n
    i = 2
    while i*i < n:
        if not primes[i]:
            i += 1
            continue
        for j in range(i*i, n, i):
            primes[j] = False
        i += 1
    count = 0
    for i in range(2, n):
        if primes[i]:
            count += 1
    return count

print(countPrimes(709486))
print(countPrimes(709486))
print(countPrimes(709486))
print(countPrimes(709486))
print(countPrimes(709486))
print(countPrimes(709486))
print(countPrimes(709486))
print(countPrimes(709486))
print(countPrimes(709486))