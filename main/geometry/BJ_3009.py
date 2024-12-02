point_1 = list(map(int, input().split()))
point_2 = list(map(int, input().split()))
point_3 = list(map(int, input().split()))

x, y = 0, 0

if point_1[0] == point_2[0]:
    x = point_3[0]
elif point_1[0] == point_3[0]:
    x = point_2[0]
else:
    x = point_1[0]

if point_1[1] == point_2[1]:
    y = point_3[1]
elif point_1[1] == point_3[1]:
    y = point_2[1]
else:
    y = point_1[1]

print(x, y)