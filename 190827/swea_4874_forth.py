for T in range(int(input())):
    print('#{0}'.format(T+1), end=' ')
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
                elif tmp1 / tmp2 - tmp1 // tmp2:
                    error = True
                    break
                s.append(tmp1 // tmp2)
        elif token == '.' and en == len(incoming)-1:
            break
        elif token == '.' and en != len(incoming)-1:
            print(s.pop(),end=' ')
        else:
            error = True
            break
    
    if error:
        print('error')
    elif len(s) > 1:
        print('error')
    else:
        print(s[0])

"""
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + / 3 + + + .

"""