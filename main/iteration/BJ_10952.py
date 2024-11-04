import sys

a, b = map(int, sys.stdin.readline().strip().split())

while a + b > 0:
    print(a + b)
    a, b = map(int, sys.stdin.readline().strip().split())