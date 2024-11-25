n, b = map(int, input().split())

result = ''
while n > 0:
    re = n % b
    if re >= 10: # 10 이상인 경우 알파벳
        result += chr(re - 10 + ord('A'))
    else:
        result += str(re)
    n //= b

print(result[::-1])