x, y, w, h = map(int, input().split())

min1 = min(x, w - x)
min2 = min(y, h - y)
print(min(min1, min2))