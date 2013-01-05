def calPrime(n):
    primes = []
    for i in xrange(3, n + 1, 2):
        max = int(i ** .5)
        for prime in primes:
            if prime > max:
                primes.append(i)
                break
            elif not i % prime:
                break
        else:
            primes.append(i)

    if n >= 2:
        primes.insert(0, 2)

    return primes

print calPrime(1000000)[10000]