t = int(input())
#
# for i in range (1, t + 1):
#     print(' ' * (t - i) + '*' * i)

for i in range (t - 1, -1, -1):
    print(' ' * i + '*' * (t - i))