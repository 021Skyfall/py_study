n = int(input())
origin = list(map(int, input().split()))
sorted_origin = sorted(origin)

rank_map = {}
rank = 0
for v in sorted_origin:
    if v not in rank_map:
        rank_map[v] = rank
        rank += 1

result = []
for k in origin:
    result.append(rank_map[k])

print(' '.join(map(str, result)))