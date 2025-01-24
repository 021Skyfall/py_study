from collections import deque

n, k = map(int, input().split())

q = deque()

for i in range(1, 1 + n):
    q.append(i)

s = ['<']

while len(q) > 1:
    for i in range(k - 1):
        q.append(q.popleft())
    s.append(str(q.popleft()) + ', ')

s. append(str(q.popleft()) + '>')
print(''.join(s))