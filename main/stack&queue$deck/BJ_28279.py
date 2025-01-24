from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

q = deque()
result = []

n = int(data[0])
for i in range(1, n + 1):
    order = data[i].split()

    if order[0] == '1':
        q.appendleft(int(order[1]))
    elif order[0] == '2':
        q.append(int(order[1]))
    elif order[0] == '3':
        result.append(q.popleft() if q else -1)
    elif order[0] == '4':
        result.append(q.pop() if q else -1)
    elif order[0] == '5':
        result.append(len(q))
    elif order[0] == '6':
        result.append(1 if not q else 0)
    elif order[0] == '7':
        result.append(q[0] if q else -1)
    elif order[0] == '8':
        result.append(q[-1] if q else -1)

print('\n'.join(map(str, result)))