import sys
sys.stdin = open('input/input_0816_2.txt', 'r')
"""
# 방법: 회문1 변형
def palindromeCheck(length):
    for row in board:
        for i in range(100 - length + 1):
            temp = row[i:i+length]
            for j in range(length // 2):
                if temp[0+j] != temp[-1-j]:
                    break
            else:
                return True
    return False

for T in range(10):
    input()
    board = []
    for _ in range(100):
        board.append(input())
    for N in range(100,0,-1):
        if palindromeCheck(N):
            result = N
            break
            
    board = list(zip(*board))
    for N in range(100,result,-1):
        if palindromeCheck(N):
            result = N
            break

    print('#{0} {1}'.format(T+1, result))
"""
# board 미리 만들어놓고 접근

def palindromeCheck(length):
    for board in boards:
        for row in board:
            for i in range(100 - length + 1):
                temp = row[i:i+length]
                for j in range(length // 2):
                    if temp[0+j] != temp[-1-j]:
                        break
                else:
                    return True
    return False

for T in range(10):
    input()
    board = []
    for _ in range(100):
        board.append(input())
    boards = [board, [*map(''.join,zip(*board))]]
    
    for N in range(100,0,-1):
        if palindromeCheck(N):
            result = N
            break

    print('#{0} {1}'.format(T+1, result))