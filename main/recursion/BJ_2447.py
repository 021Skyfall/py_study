def solution(x):
    if x == 1:
        return ['*']
    star = solution(x // 3)

    result = []
    for i in star:
        result.append(i * 3)
    for j in star:
        result.append(j + ' ' * (x // 3) + j)
    for k in star:
        result.append(k * 3)

    return result

n = int(input())
print('\n'.join(solution(n)))