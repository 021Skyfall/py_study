from collections import deque

n = int(input())

q = deque()
for i in range(1, n + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()  # O(1) 시간 복잡도로 첫 번째 요소 제거
    q.append(q.popleft())  # O(1) 시간 복잡도로 첫 번째 요소를 제거하고 뒤에 추가

print(q[0])