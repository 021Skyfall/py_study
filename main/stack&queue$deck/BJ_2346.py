from collections import deque

n = int(input())
arr = list(map(int, input().split()))

q = deque()
for i in range(1, n):
    q.append((i + 1, arr[i]))

result = []
in_p = arr[0]
result.append('1')
while len(q) > 0:
    if in_p > 0:
        for i in range(1, in_p):
            q.append(q.popleft())
        next_p = q.popleft()
        in_p = next_p[1]
        result.append(str(next_p[0]))
    else:
        for i in range(1, -in_p):
            q.appendleft(q.pop())
        next_p = q.pop()
        in_p = next_p[1]
        result.append(str(next_p[0]))

print(' '.join(result))