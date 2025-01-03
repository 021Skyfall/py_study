import math

max_r = 1000000
isPrime = [False] * (max_r + 1)
isPrime[0] = isPrime[1] = True

for i in range(2, int(math.sqrt(max_r)) + 1):
    if not isPrime[i]:
        for j in range(i * i, max_r + 1, i):
            isPrime[j] = True

primes = [i for i in range(2, max_r + 1) if not isPrime[i]]

t = int(input())

while t > 0:
    n = int(input())
    count = 0
    left, right = 0, len(primes) - 1

    while left <= right:
        sum_primes = primes[left] + primes[right]
        if sum_primes < n:
            left += 1
        elif sum_primes > n:
            right -= 1
        else:
            count += 1
            left += 1
            right -= 1

    print(count)
    t -= 1