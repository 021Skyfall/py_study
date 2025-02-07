def solution(x, start, end):
    if x == 1:
        print(start, end)
        return

    solution(x - 1, start, 6 - start - end) # 1단
    print(start, end) # 2단
    solution(x - 1, 6 - start - end, end) # 3단

n = int(input())
print(2 ** n - 1)
solution(n , 1, 3)

# 참고 https://study-all-night.tistory.com/6