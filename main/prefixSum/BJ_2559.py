n, k = map(int, input().split())
temp = list(map(int, input().split()))

prefix_sum = [0]*(n + 1)

answer = (n + 1) * -100

for i in range(1, n + 1):
    prefix_sum[i] += prefix_sum[i - 1]+temp[i - 1]

for i in range(1, n - k + 2):
    temp_sum = prefix_sum[i + k - 1] - prefix_sum[i - 1]
    if temp_sum > answer:
        answer = temp_sum

print(answer)