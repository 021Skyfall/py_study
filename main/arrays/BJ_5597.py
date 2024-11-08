arr = [0] * 31

for _ in range(28):
    x = int(input())
    arr[x] = 1

for i in range(1, len(arr)):
    if arr[i] != 1:
        print(i)