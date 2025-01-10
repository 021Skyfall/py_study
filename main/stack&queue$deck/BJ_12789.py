n = int(input())
stack = []
start = 1

elements = list(map(int, input().split()))

for x in elements:
    stack.append(x)

    while len(stack) > 0 and stack[-1] == start:
        stack.pop()
        start += 1

if len(stack) == 0:
    print("Nice")
else:
    print("Sad")