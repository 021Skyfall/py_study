import sys

stack = []
output = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    order = list(map(int, sys.stdin.readline().strip().split()))

    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        output.append(stack.pop() if stack else -1)
    elif order[0] == 3:
        output.append(len(stack))
    elif order[0] == 4:
        output.append(1 if not stack else 0)
    elif order[0] == 5:
        output.append(stack[-1] if stack else -1)

print('\n'.join(map(str, output)))
