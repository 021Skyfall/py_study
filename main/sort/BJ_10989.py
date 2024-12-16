import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            print(i)

# 빠른 입력
# 빠른 출력 시 값을 담아서 출력하고자 하니 메모리가 채워져서 메모리 초과됨 -> 출력값을 메모리에 할당하지 않고 바로 출력하는 것으로 해결