# swexpertacademy 4869

"""
갯수
크기 n인 직사각형

목표 길이

"""
"""
def DFS(target):
    stack = []
    length = 0
    count = 0
    twos = 0
    visited = [0, 0]
    for i in range(2):
        stack.append([i+1])
        while len(stack):
            print(stack)
            v = stack.pop()
            w = v.pop()
            if v:
                stack.append(v)
            length += w
            if not w % 2:
                twos += 1

            left = target - length
            if not left:
                print(' ',end=' ')
                print(length, twos)
                count += 2 * twos
                length -= w
            elif left == 1:
                stack.append([1])
            else:
                stack.append([1,2])
    
    print(count, twos)
    
    return None

DFS(3)

DFS(5)

DFS(7)
"""

# 1 재귀 | 0.15776s

def rdfs(target):
    if target == 1:
        return 1
    elif target == 2:
        return 3
    return rdfs(target-1) + 2 * rdfs(target-2)

for T in range(int(input())):
    target = int(input()) // 10
    print('#{0} {1}'.format(T+1,rdfs(target)))

# 2 Stack ???

def sdfs(target):
    result = 0
    count = 1
    path = []
    if target == 1:
        stack = [[1]]
    else:
        stack = [[1,2]]

    # stack은 이전 경로의 방문하지 않은 노드 보관
    # 현재 위치에서 가능한 노드(1개 혹은 2개)를 쌓고 바로 pop하여 사용
    while stack:
        if sum(path) == target:
            result += count
            count //= path.pop()
        
        # 다음 단계 꺼내기
        nodes = stack.pop()
        v = nodes.pop()
        stack.append(nodes)

        if not v % 2:
            count *= 2
        path.append(v)
        
        left = target - sum(path)
        if stack[-1]:
            if left > 1:
                stack.append([1,2])
            elif left == 1:
                stack.append([1])
        else:
            stack.pop()

    return result

print(sdfs(3))


# for T in range(int(input())):
#     target = int(input()) // 10
#     print('#{0} {1}'.format(T+1, sdfs(target)))
