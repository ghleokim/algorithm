for T in range(int(input())):
    s = []
    error = False
    incoming = input().split()
    for en, token in enumerate(incoming):
        if token.isdigit():
            s.append(int(token))
        elif token in '+-*/':
            if len(s) < 2:
                error = True
                break
            tmp2, tmp1 = s.pop(), s.pop()
            if token == '+':
                s.append(tmp1 + tmp2)
            elif token == '-':
                s.append(tmp1 - tmp2)
            elif token == '*':
                s.append(tmp1 * tmp2)
            else:
                if tmp2 == 0:
                    error = True
                    break
                s.append(tmp1 // tmp2)
        elif token == '.' and en == len(incoming)-1:
            break
        else:
            error = True
            break

    if error:
        print('#{0} error'.format(T+1))
    else:
        print('#{0} {1}'.format(T+1, s[0]))
