"""

수식으로 만들 수 있는 최댓값 - 최솟값

"""
"""
# 실패: runtime error(memory limit exceed)

def calc(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        return int(num1 / num2)
 
 
def check(comb):
    num = 0
    for k, n in enumerate(comb):
        num += n * 4 ** k
    return num
 
 
def solve(cur_res, depth=1, choice=[]):
    global max_res
    global min_res
 
    if depth == len(nums):
        if cur_res < min_res: min_res = cur_res
        if cur_res > max_res: max_res = cur_res
        return 0
 
    for i in range(len(op)):
        next_res = cur_res
        if not visited[i]:
            visited[i] = 1
            choice.append(op[i])
 
            next_res = calc(cur_res, nums[depth], op[i])
            check_val = check(choice)
 
            if not dp[check_val]:
                solve(next_res, depth+1, choice)
                dp[check_val] = 1
 
            choice.pop()
            visited[i] = 0
 
 
for T in range(int(input())):
    N = int(input())
    op_input = [*map(int,input().split())]
    nums = [*map(int,input().split())]
 
    op = [None for _ in range(N-1)]
    dp = [0 for _ in range(4 ** (N-1))]
 
    count = 0
    for i in range(4):
        for j in range(op_input[i]):
            op[count] = i
            count += 1
 
    min_res = 9 ** N
    max_res = -9 ** (N-1)
    visited = [0 for _ in range(N-1)]
 
    solve(nums[0])
 
    print('#', end='')
    print(T+1, max_res-min_res)
"""
# ------------------------------------- #

# 성공

def calc(num1, num2, oper):
    # calculate
    if oper == 0:
        return num1 + num2
    elif oper == 1:
        return num1 - num2
    elif oper == 2:
        return num1 * num2
    else:
        return int(num1 / num2)

### lambda로 dict함수를 만드는 것이 조금 더 빠르다.
calc2 = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: lambda x, y: int(x / y)
}

def solve(cur_res, depth=1):
    global max_res
    global min_res
    
    # return
    if depth == len(nums):
        if cur_res < min_res: min_res = cur_res
        if cur_res > max_res: max_res = cur_res
        return 0

    # seek
    for oper, val in enumerate(oper_input):
        if val == 0: continue
        oper_input[oper] -= 1
        next_res = calc(cur_res, nums[depth], oper)
        
        solve(next_res, depth+1)
        oper_input[oper] += 1

# --------------------------- #

for T in range(int(input())):
    # input
    N = int(input())
    oper_input = [*map(int,input().split())]
    nums = [*map(int,input().split())]
    
    # initialize
    min_res = 9 ** N
    max_res = -9 ** (N-1)

    # solve
    solve(nums[0])

    # print
    print('#', end='')
    print(T+1, max_res-min_res)
