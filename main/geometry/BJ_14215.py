x, y, z = map(int, input().split())

max_all = 0

if x > y:
    if y > z:
        max_all = x
    else:
        max_all = max(x, z)
else:
    max_all = max(y, z)

if x + y + z - max_all > max_all:
    print(x + y + z)
else:
    print((x + y + z - max_all) * 2 - 1)