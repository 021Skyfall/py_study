n, m = map(int, input().split())

arr = []

for i in range(n):
    r = list(map(int, input().split()))
    arr.append(r)

for i in range(n):
    add = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] += add[j]

for row in arr:
    print(' '.join(map(str, row)))