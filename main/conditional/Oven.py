h, m = map(int, input().split())
t = int(input())

total = h * 60 + m + t

h = (total // 60) % 24
m = total % 60

print(f"{h} {m}")