arr = [int(char) for char in input()]

arr.sort(reverse=True)

print(''.join(map(str, arr)))