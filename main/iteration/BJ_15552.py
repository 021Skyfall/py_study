import sys

t = int(sys.stdin.readline().strip())

for i in range (0, t):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(a + b)

# strip = 개행 문자 제거 / input() 은 자동으로 개행문자가 제거됨
# input() 은 예외 발생 X, sys.stdin.readline() 은 입력을 한번에 받기 때문에 형식이 맞지 않으면 예외 발생