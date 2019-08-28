# 1 순서대로
"""
3+(4+5)*6+7

# incoming priority
icp = {
    '(': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}
# instack priority
isp = {
    '(': 0,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}


for T in range(10):
    N, incoming = int(input()), input()

    stack = [0 for _ in range(N)]
    top = -1

    calc = [0 for _ in range(N)]
    ctop = -1

    # conversion into postfix expression
    for token in incoming:
        if ord(token) >= 48 and ord(token) <= 57:
            ctop += 1
            calc[ctop] = int(token)
        elif token == ')':
            while top != -1:
                if stack[top] == '(':
                    stack[top] = 0
                    top -= 1
                    break
                else:
                    ctop += 1
                    calc[ctop] = stack[top]
                    stack[top] = 0
                    top -= 1
        else:
            if top == -1:
                top += 1
                stack[top] = token
                continue
            else:
                while top != -1:
                    if icp[token] > isp[stack[top]]:
                        break
                    else:
                        ctop += 1
                        calc[ctop] = stack[top]
                        stack[top] = 0
                        top -= 1
                top += 1
                stack[top] = token

    while top != -1:
        ctop += 1
        calc[ctop] = stack[top]
        stack[top] = 0
        top -= 1

    # stack 재활용
    for c in calc:
        if type(c) == int:
            top += 1
            stack[top] = c
        else:
            tmp1, tmp2 = stack[top-1], stack[top]
            stack[top-1], stack[top] = 0, 0
            top -= 2
            if c == '+':
                res = tmp1 + tmp2
            elif c == '-':
                res = tmp1 - tmp2
            elif c == '*':
                res = tmp1 * tmp2
            else:
                res = tmp1 // tmp2
            top += 1
            stack[top] = res

    print('#{0} {1}'.format(T+1, stack[0]))
"""
"""
# 150 ms
# incoming priority
icp = {'(': 3,'*': 2,'/': 2,'+': 1,'-': 1}
# instack priority
isp = {'(': 0,'*': 2,'/': 2,'+': 1,'-': 1}

# for stack and calc
def push(tar):
    global top;top+=1;stack[top]=tar

def cpush(tar):
    global ctop;ctop+=1;calc[ctop]=tar

# only for stack
def pop():
    global top;top-=1;r,stack[top+1]=stack[top+1],0
    return r

for T in range(10):
    N = int(input())
    stack, calc = [0 for _ in range(N)], [0 for _ in range(N)]
    top, ctop = -1, -1
    # conversion into postfix expression
    for token in input():
        if all((ord(token)>=48,ord(token)<=57)): cpush(int(token))
        elif token == ')':
            while top != -1:
                if stack[top] == '(': pop(); break
                else: cpush(pop())
        else:
            if top == -1: push(token); continue
            else:
                while top != -1:
                    if icp[token] > isp[stack[top]]: break
                    else: cpush(pop())
                push(token)
    while top != -1: cpush(pop())

    # stack 재활용
    for c in calc:
        if type(c) == int: push(c)
        else:
            tmp2, tmp1 = pop(), pop()
            if c == '+': res = tmp1 + tmp2
            elif c == '-': res = tmp1 - tmp2
            elif c == '*': res = tmp1 * tmp2
            else: res = tmp1 // tmp2
            push(res)

    print('#{0} {1}'.format(T+1, stack[0]))
"""

# library
# incoming priority
icp = {'(': 3,'*': 2,'/': 2,'+': 1,'-': 1}
# instack priority
isp = {'(': 0,'*': 2,'/': 2,'+': 1,'-': 1}

for T in range(10):
    N = int(input())
    stack, calc = [], []
    # conversion into postfix expression
    for token in input():
        if ord(token)>47:
            calc.append(int(token))
        elif token == ')':
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    calc.append(stack.pop())
        else:
            if not stack:
                stack.append(token)
                continue
            else:
                while stack:
                    if icp[token] > isp[stack[-1]]: break
                    else:
                        calc.append(stack.pop())
                stack.append(token)
    while stack:
        calc.append(stack.pop())
    # stack 재활용
    for c in calc:
        if type(c) == int:
            stack.append(c)
        else:
            tmp2, tmp1 = stack.pop(), stack.pop()
            if c == '+': res = tmp1 + tmp2
            elif c == '-': res = tmp1 - tmp2
            elif c == '*': res = tmp1 * tmp2
            else: res = tmp1 // tmp2
            stack.append(res)

    print('#{0} {1}'.format(T+1, stack[0]))