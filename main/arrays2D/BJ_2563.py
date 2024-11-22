n = int(input())

# False 로 초기화 100*100 배열 (도화지)
arr = [[False] * 100 for _ in range(100)]

result = 0

for i in range(n):
    x, y = map(int, input().split())

    for j in range(x, x + 10):
        for k in range(y, y + 10):
            if not arr[j][k]:
                arr[j][k] = True
                result += 1 # 중복 제외

print(result)