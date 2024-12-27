from collections import Counter

n = int(input())
list_1 = list(map(int, input().split()))
count_1 = Counter(list_1)

m = int(input())
list_2 = list(map(int, input().split()))

result = [count_1[i] for i in list_2]

print(' '.join(map(str, result)))