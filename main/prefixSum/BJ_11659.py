n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
tmp = 0

for num in nums:
    tmp += num
    sums.append(tmp)

results = []
for _ in range(m):
    i, j = map(int, input().split())
    results.append(sums[j] - sums[i - 1])

print('\n'.join(map(str, results)))