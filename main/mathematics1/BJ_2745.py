n, b = input().split()
b = int(b)

tmp = 1
result = 0
for i in range(len(n), 0, -1):
    c = n[i - 1]
    if 'A' <= c <= 'Z':
        result += (ord(c) - ord('A') + 10) * tmp
    else:
        result += (ord(c) - ord('0')) * tmp
    tmp *= b

print(result)

'''
n, b = input().split()
b = int(b)

result = sum((ord(c) - ord('A') + 10
              if 'A' <= c <= 'Z'
              else ord(c) - ord('0'))
             * (b ** i) for i, c in enumerate(reversed(n)))

print(result)
'''

'''
n, b = input().split()
print(int(n, int(b)))
'''