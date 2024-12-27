n = int(input())

# 딕셔너리
result = {}

for _ in range(n):
    name, command = input().split()

    if command == "leave":
        result.pop(name, None)
    else:
        result[name] = None

print('\n'.join(map(str, sorted(result.keys(), reverse=True))))