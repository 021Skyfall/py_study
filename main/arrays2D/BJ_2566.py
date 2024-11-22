arr = []

for i in range(9):
    r = list(map(int, input().split()))
    arr.append(r)

max_value = 0
max_position = (0, 0)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] >= max_value:
            max_value = arr[i][j]
            max_position = (i + 1, j + 1)

print(max_value)
print(*max_position)

'''
문제가 이상함
max 가 중복되는 경우 그 중 하나만 출력하면 된다
라고 되어 있는데
실제로는 마지막으로 나온 큰 수를 리턴해야함
그래서 max value 조건식을 초과에서 이상으로 변경함
'''