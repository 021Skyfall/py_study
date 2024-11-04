# n = int(input())
#
# count = n // 4
#
# strings = []
# for i in range (0, count):
#     strings.append("long ")
# strings.append("int")
#
# result = ''.join(strings)
# print(result)

n = int(input())
count = n // 4

result = "long " * count + "int"
print(result)