n = int(input())

arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda p: (p[0], p[1]))

for x, y in arr:
    print(x, y)