arr = []

for _ in range(10):
    n = int(input())
    x = n % 42
    arr.append(x)

print(len(set(arr)))