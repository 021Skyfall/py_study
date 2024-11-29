def is_prime(x):
    if x == 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False

    return True

n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(n):
    if is_prime(arr[i]):
        count += 1

print(count)


