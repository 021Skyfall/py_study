arr = list(map(int, input().split()))
compare = [1, 1, 2, 2, 2, 8]

result = []

for i in range(len(arr)):
    if arr[i] == compare[i]:
        result.append(0)
    else:
        result.append(compare[i] - arr[i])


print(' '.join(map(str, result)))

# arr = list(map(int, input().split()))
# compare = [1, 1, 2, 2, 2, 8]
#
# # 리스트 컴프리핸션
# result = [
#     0 if arr[i] == compare[i] else compare[i] - arr[i]
#     for i in range(len(arr))
# ]
#
# print(' '.join(map(str,result)))