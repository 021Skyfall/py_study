# ar = [-1] * 26
#
# s = input()
#
# for i in range(len(s)):
#     ch = s[i]
#     idx = ord(ch) - ord('a')
#     if ar[idx] == -1:
#         ar[idx] = i
#
# print(*ar)

ar = [-1] * 26
s = input()

for i, ch in enumerate(s):
    idx = ord(ch) - ord('a')
    if ar[idx] == -1:
        ar[idx] = i

print(*ar)