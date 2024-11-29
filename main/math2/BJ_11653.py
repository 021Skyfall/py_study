n = int(input())
k = 2

while k * k <= n:
    if n % k == 0:
        print(k)
        n /= k
    else:
        k += 1

if n > 1:
    print(int(n))