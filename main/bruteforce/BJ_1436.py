import sys

def func(n):
    count = 1
    prev_digit = 0
    num = 0

    while True:
        if (prev_digit % 10000) // 10 == 666 and prev_digit % 10 != 6:
            for i in range(1000):
                if count == n:
                    print(prev_digit * 1000 + num)
                    return
                num += 1
                count += 1
            prev_digit += 1
        elif prev_digit % 1000 == 666:
            num = 0
            for i in range(1000):
                if count == n:
                    print(prev_digit * 1000 + num)
                    return
                count += 1
                num += 1
            prev_digit += 1
        elif prev_digit % 100 == 66:
            num = 600
            for i in range(100):
                if count == n:
                    print(prev_digit * 1000 + num)
                    return
                count += 1
                num += 1
            prev_digit += 1
        elif prev_digit % 10 == 6:
            num = 660
            for i in range(10):
                if count == n:
                    print(prev_digit * 1000 + num)
                    return
                num += 1
                count += 1
            prev_digit += 1
        else:
            num = 666
            if count == n:
                print(prev_digit * 1000 + num)
                return
            count += 1
            prev_digit += 1

n = int(sys.stdin.read().strip())
if n > 1:
    func(n)
else:
    print(666)