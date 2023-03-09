import math

def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            factors.append((i, cnt))

    if n > 1:
        factors.append((n, 1))
    return factors

def main():
    c = int(input())

    for test in range(c):
        n = int(input())
        factors = prime_factorization(n)
        factors.sort(key=lambda x: x[1])

        primes = [item[0] for item in factors]
        powers = [item[1] for item in factors]

        res = 0
        currProduct = math.prod(primes)
        prevPower = 0

        while len(powers):
            currPrime = primes.pop(0)
            currPower = powers.pop(0)
            res += currProduct * (currPower - prevPower)
            prevPower = currPower
            currProduct //= currPrime
        
        print(res)

if __name__ == '__main__':
    main()