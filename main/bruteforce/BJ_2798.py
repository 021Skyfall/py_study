import sys

input_data = sys.stdin.read
data = input_data().splitlines()

n, m = map(int, data[0].split())
nums = list(map(int, data[1].split()))

result = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            temp = nums[i] + nums[j] + nums[k]

            if temp == m:
                result = temp
                break

            if result < temp < m:
                result = temp

print(result)