n = int(input())
stack = []

for _ in range(n):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)

result = 0
for i in stack:
    result += i

print(result)