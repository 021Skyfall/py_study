n = int(input())

root = 1
r_range = 2

if n == 1:
    print(1)
else:
    while r_range <= n:
        r_range += (6 * root)
        root += 1
    print(root)