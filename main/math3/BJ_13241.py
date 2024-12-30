def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

n, m = map(int, input().split())

print(int((n * m) / gcd(n, m)))