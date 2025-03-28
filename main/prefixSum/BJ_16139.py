import sys

s = sys.stdin.readline().rstrip()
n = len(s)

# 각 문자에 대한 누적 카운트 배열 초기화
count = [[0] * 26 for _ in range(n + 1)]

# 누적 카운트 계산
for i in range(n):
    count[i + 1] = count[i][:]
    count[i + 1][ord(s[i]) - ord('a')] += 1

q = int(sys.stdin.readline().rstrip())
results = []

for _ in range(q):
    alpha, l, r = sys.stdin.readline().rstrip().split()
    l, r = int(l), int(r)
    answer = count[r + 1][ord(alpha) - ord('a')] - count[l][ord(alpha) - ord('a')]
    results.append(str(answer))

sys.stdout.write("\n".join(results) + "\n")