for T in range(int(input())):
    incoming = input().split()

    stack = [0 for _ in range(256)]
    top = -1
    error = False

    for en, token in enumerate(incoming):
        if token.isdigit():
            top += 1
            stack[top] = int(token)
        elif token in '+-*/':
            if top == 0:
                error = True
                break
            
            tmp2 = stack[top]
            top -= 1
            tmp1 = stack[top]
            top -= 1

            if token == '+':
                res = tmp1 + tmp2
                top += 1
                stack[top] = res
            elif token == '-':
                res = tmp1 - tmp2
                top += 1
                stack[top] = res
            elif token == '*':
                res = tmp1 * tmp2
                top += 1
                stack[top] = res
            else:
                res = tmp1 // tmp2
                top += 1
                stack[top] = res
        elif token == '.':
            if en != len(incoming)-1:
                error = True
            break
        else:
            error = True
            break

    if token[-1] != '.':
        error = True

    if error:
        print('#{0} error'.format(T+1))
    else:
        print('#{0} {1}'.format(T+1, res))

