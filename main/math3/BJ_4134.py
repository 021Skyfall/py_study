def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())
    while 1:
        if is_prime(n):
            print(n)
            break
        n += 1