def is_prime(x):
    if x == 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False

    return True

m = int(input())
n = int(input())

result = []

for i in range(m, n + 1):
    if is_prime(i):
        result.append(i)

print(f"{sum(result)}\n{result[0]}" if len(result) else -1)