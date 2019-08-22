# swexpertacademy 4873

"""
while i < len(string)

1 stack이 비어있으면 stack.push, top += 1
2 stack[top]과 들어오는 string[i] 비교
    2-1 같으면 i += 1, stack.pop, top -= 1,
    2-2 다르면 i += 1, stack.push, top += 1
"""

# 1 스택 활용 | 0.14595s
for T in range(int(input())):
    string = input()
    length = len(string)
    i = 0

    stack = [0] * length
    top = -1

    while i < len(string):
        if top == -1:
            top += 1
            stack[top] = string[i]
            i += 1
        if stack[top] == string[i]:
            stack[top] = 0
            top -= 1
            i += 1
        else:
            top += 1
            stack[top] = string[i]
            i += 1


    print('#{0} {1}'.format(T+1, top+1))


# 2 index로 접근, del | 0.14880s
for T in range(int(input())):
    s = [*input()]
    i = 0
    length = len(s)

    while i < length-1:
        if s[i] == s[i+1]:
            del s[i:i+2]
            length = len(s)
            if i: i -= 1
        else: i += 1

    print('#{0} {1}'.format(T+1, i+1))
