def sum_of(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input())
result = 0

for i in range(1, n):
    if i + sum_of(i) == n:
        result = i
        break

print(result)