while 1:
    angle_lengths = list(map(int, input().split()))
    x = angle_lengths[0]
    y = angle_lengths[1]
    z = angle_lengths[2]
    sum_lengths = x + y + z

    if sum_lengths == 0:
        break

    max_all = 0
    secondary = 0
    for i in range(3):
        cur = angle_lengths[i]

        if cur > max_all:
            secondary = max_all
            max_all = cur
        elif cur > secondary:
            secondary = cur

    rest = (x + y + z) - max_all

    if max_all >= rest:
        print("Invalid")
    else:
        if x == z and y == z:
            print("Equilateral")
        elif x == y or x == z or y == z:
            print("Isosceles")
        else:
            print("Scalene")
