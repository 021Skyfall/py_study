import math

while True:
    n = int(input())

    if n == 0:
        break

    isPrime = [False] * (2 * n + 1)
    isPrime[0] = isPrime[1] = True
    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if not isPrime[i]:
            for j in range(i * i, 2 * n + 1, i):
                isPrime[j] = True

    count = 0
    for i in range(n + 1, 2 * n + 1):
        if not isPrime[i]:
            count += 1

    print(count)