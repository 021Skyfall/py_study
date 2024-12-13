import sys

n = int(sys.stdin.read().strip())

max_bags_of_5 = n // 5
min_bags = float('inf')

for i in range(max_bags_of_5, -1, -1):
    remain = n - i * 5
    if remain % 3 == 0:
        bags = i + remain // 3
        min_bags = min(min_bags, bags)

if min_bags == float('inf'):
    print(-1)
else:
    print(min_bags)