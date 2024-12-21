n = int(input())

arr = []

for _ in range(n):
    arr.append(input())

# 길이로 정렬하고, 길이가 같을 경우 사전순으로 정렬
arr.sort(key=lambda x: (len(x), x))

# 중복 제거
pre = ""
result = []
for s in arr:
    if s != pre:
        pre = s
        result.append(s)

print("\n".join(result))