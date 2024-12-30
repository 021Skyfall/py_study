def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

gcd_result = arr[1] - arr[0]

for i in range(2, n):
    gcd_result = gcd(gcd_result, arr[i] - arr[i - 1])

count = 0
for i in range(1, n):
    count = count + ((arr[i] - arr[i - 1]) / gcd_result) - 1

print(int(count))