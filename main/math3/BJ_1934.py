def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(int((n * m) / gcd(n, m)))