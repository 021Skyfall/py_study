result = []

while True:
    st = input()

    if st == '.':
        break

    stack = []
    isBalanced = True

    for i in range(len(st)):
        ch = st[i]

        if ch == '(' or ch == '[':
             stack.append(ch)
        elif ch == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                isBalanced = False
                break
        elif ch == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                isBalanced = False
                break

    if len(stack) > 0 or not isBalanced:
        result.append("no")
    else:
        result.append("yes")

print('\n'.join(result))