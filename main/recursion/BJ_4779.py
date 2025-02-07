def solution(x):
    if x == 1:
        return '-'
    else:
        left = solution(x // 3)
        middle = ' ' * (x // 3)
        return left + middle + left

while True:
    try:
        n = int(input())

        result = solution(3 ** n)
        print(result)
    except EOFError:
        break

# 참고 https://wikidocs.net/206410