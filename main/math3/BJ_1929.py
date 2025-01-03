import math

m, n = map(int, input().split())

isPrime = [False] * (n + 1)
isPrime[0] = isPrime[1] = True

for i in range(2, int(math.sqrt(n)) + 1):
    if not isPrime[i]:
        for j in range(i * i, n + 1, i):
            isPrime[j] = True

for i in range(m, n + 1):
    if not isPrime[i]:
        print(i)