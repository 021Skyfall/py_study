s = input().upper()

arr = [0] * 26
for i in range(len(s)):
    arr[ord(s[i]) - ord('A')]+= 1

m = 0
ch = '?'

for i in range(26):
    if arr[i] > m:
        m = arr[i]
        ch = chr(i + 65)
    elif arr[i] == m:
        ch = '?'

print(ch)

# from collections import Counter
#
# s = input().upper()
# # 문자의 빈도수 계산
# counter = Counter(s)
#
# # 가장 많이 등장한 문자 찾기
# max_count = max(counter.values())
# most_chars = [char for char, count in counter.items() if count == max_count]
#
# if len(most_chars) == 1:
#     print(most_chars[0])
# else:
#     print('?')

# counter = 각 문자 빈도 계산 함수