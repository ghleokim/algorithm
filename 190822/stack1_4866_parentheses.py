# swexpertacademy 4866

# 1 stack with string | 0.14843s
for T in range(int(input())):

    STACK = [0] * 50
    top = -1
    result = 0

    for v in input():
        if v == '(' or v == '{':
            top += 1
            STACK[top] = v
        elif v == ')':
            w = STACK[top]
            STACK[top] = 0
            top -= 1
            if w != '(':
                break
        elif v == '}':
            w = STACK[top]
            STACK[top] = 0
            top -= 1
            if w != '{':
                break
    else:
        print(top)
        if top == -1:
            result = 1

    print('#{0} {1}'.format(T+1, result))


# 2 stack with ord() | 0.15529s
for T in range(int(input())):

    STACK = [0] * 50
    top = -1
    result = 0

    for v in input():
        o = ord(v)
        if o == 40 or o == 123:
            top += 1
            STACK[top] = o
        elif o == 41:
            w = STACK[top]
            STACK[top] = 0
            top -= 1
            if w != o-1:
                break
        elif o == 125:
            w = STACK[top]
            STACK[top] = 0
            top -= 1
            if w != o-2:
                break
    else:
        if top == -1:
            result = 1

    print('#{0} {1}'.format(T+1, result))