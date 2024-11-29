while 1:
    x, y = map(int, input().split())

    if x + y == 0:
        break
    elif x % y == 0:
        print('multiple')
    elif y % x == 0:
        print('factor')
    else:
        print('neither')