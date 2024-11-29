n, k = map(int, input().split())

arr = []

for i in range(n + 1):
    if i == 0:
        continue
    elif n % i == 0:
        arr.append(i)

print(arr[k - 1] if k <= len(arr) else 0)