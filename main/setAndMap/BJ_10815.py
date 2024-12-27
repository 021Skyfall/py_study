n = int(input())
set_1 = set(map(int, input().split()))
m = int(input())
list_2 = list(map(int, input().split()))

result = [1 if i in set_1 else 0 for i in list_2]

print(' '.join(map(str, result)))