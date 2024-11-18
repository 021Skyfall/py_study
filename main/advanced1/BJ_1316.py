n = int(input())
count = 0

for i in range(n):
    s = input()
    check = [False] * 26
    prev = None
    is_group = True

    for ch in s:
        cur = ord(ch)
        if prev != cur:
            if check[cur - ord('a')]:
                is_group = False
                break
            check[cur - ord('a')] = True
            prev = cur

    if is_group:
        count += 1

print(count)