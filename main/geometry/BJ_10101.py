x = int(input())
y = int(input())
z = int(input())

sum_angle = x + y + z

if sum_angle == 180:
    if x == y == z:
        print("Equilateral")
    elif x == y or x == z or y == z:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
