n = int(input())
result = []

for _ in range(n):
    st = input()
    stack = []
    for ch in st:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(ch)
                break

    if len(stack) == 0:
        result.append("YES")
    else:
        result.append("NO")

print('\n'.join(result))