import sys

input = sys.stdin.read
data = input().strip().splitlines()

n, m = map(int, data[0].split())
arr = [[True if char == 'W' else False for char in line] for line in data[1:n+1]]

min_count = 64
n_row = n - 7
m_col = m - 7

def find(arr, x, y):
    end_x = x + 8
    end_y = y + 8
    count = 0

    TF = arr[x][y]

    for i in range(x, end_x):
        for j in range(y, end_y):
            if arr[i][j] != TF:
                count += 1
            TF = not TF
        TF = not TF

    count = min(count, 64 - count)
    return count

for i in range(n_row):
    for j in range(m_col):
        min_count = min(min_count, find(arr, i, j))

print(min_count)