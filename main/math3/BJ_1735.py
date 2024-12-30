def gcd(x, y):
    while y == 0:
        return x
    return gcd(y, x % y)

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

result_a = (a1 * b2) + (a2 * b1)
result_b = b1 * b2

gcd_result = gcd(result_a, result_b)
print(int(result_a / gcd_result), int(result_b / gcd_result))