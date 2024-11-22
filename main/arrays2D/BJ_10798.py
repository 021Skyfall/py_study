# 5*15 배열 초기화
arr = [[''] * 15 for _ in range(5)]

# 입력
for i in range(5):
    s = input().rstrip()  # 입력받은 문자열의 오른쪽 공백 제거
    for j in range(len(s)):
        arr[i][j] = s[j]  # 각 문자를 배열에 저장

result = ''

for i in range(len(arr[0])):
    for j in range(len(arr)):
        result += str(arr[j][i])

print(result)