import sys

input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
arr = [False] * 2000001

for _ in range(n):
    arr[int(input()) + 1000000] = True

result = []
for i in range(len(arr)):
    if arr[i]:
        result.append(i - 1000000)

output('\n'.join(map(str, result)) + '\n')

# list는 내장형 함수와 겹치기 때문에 변수명으로 사용하면 출력값이 달라짐
# 빠른 입출력이 없으면 시간초과