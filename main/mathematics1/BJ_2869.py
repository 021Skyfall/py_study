a, b, v = map(int, input().split())

count = (v - b) / (a - b)
if (v - b) % (a - b) != 0:
    count += 1

print(int(count))