total = int(input())
scores = list(map(int, input().split()))

m = max(scores)
sum_scores = sum(scores)

average = (sum_scores / m) * 100 / total

print(average)