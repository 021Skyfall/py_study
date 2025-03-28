import sys

n, m = map(int, sys.stdin.readline().split())
map_ = [[0] * 1206 for _ in range(1206)]  # i, j까지 합

for i in range(1, n + 1):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n + 1):
        temp = row[j - 1]
        map_[i][j] = map_[i - 1][j] + map_[i][j - 1] + temp - map_[i - 1][j - 1]
        # i, j까지의 합 구하기

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = map_[x2][y2] - map_[x1 - 1][y2] - map_[x2][y1 - 1] + map_[x1 - 1][y1 - 1]  # 구간 합 계산
    print(result)