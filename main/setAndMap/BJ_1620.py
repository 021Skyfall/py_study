n, m = map(int, input().split())

pokedex = {}

# 딕셔너리는 키를 기준으로만 조회 가능
for i in range(1, n + 1):
    name = input()
    pokedex[name] = i
    pokedex[i] = name

results = []
for j in range(n + 1, n + 1 + m):
    key = input()
    if key.isdigit():
        results.append(pokedex[int(key)])
    else:
        results.append(pokedex[key])

print("\n".join(map(str, results)))