n, m = map(int, input().split())

arr_1 = []
arr_2 = []

for _ in range(n):
    arr_1.append(input())
for _ in range(m):
    arr_2.append(input())

result = [1 if i in arr_1 else 0 for i in arr_2]

print(sum(result))