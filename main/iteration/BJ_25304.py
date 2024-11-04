total = int(input())
n = int(input())

spend = 0
for i in range (0, n):
    a, b = map(int, input().split())
    spend += (a * b)

if spend == total:
    print("Yes")
else:
    print("No")