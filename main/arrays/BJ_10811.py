import sys

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())

arr = list(range(1, n + 1))

for i in range(1, m + 1):
    x, y = map(int, data[i].split())
    x -= 1
    y -= 1
    while x < y:
        arr[x], arr[y] = arr[y], arr[x]
        x += 1
        y -= 1

print(" ".join(map(str, arr)))