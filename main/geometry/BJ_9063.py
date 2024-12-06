import sys

n = int(input())

max_1, max_2 = - sys.maxsize - 1, - sys.maxsize - 1
min_1, min_2 = sys.maxsize, sys.maxsize

for i in range(n):
    cur = list(map(int, input().split()))
    x, y = cur[0], cur[1]

    max_1 = max(max_1, x)
    max_2 = max(max_2, y)

    min_1 = min(min_1, x)
    min_2 = min(min_2, y)

print((max_1 - min_1) * (max_2 - min_2))