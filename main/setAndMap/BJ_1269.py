n, m = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

set_1 = set(arr_1)
set_2 = set(arr_2)

s_d = set_1.symmetric_difference(set_2)

print(len(s_d))