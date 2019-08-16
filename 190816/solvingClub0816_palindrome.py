"""
길이 1: 무조건 회문

길이 2 - 1번 검사
길이 3 - 1번 검사

길이 4 - 2번 검사
길이 5 - 2번 검사

길이 6 - 3번 검사
길이 7 - 3번 검사

길이 8 - 4번 검사
"""
import sys
sys.stdin = open('input/input_0816_1.txt', 'r')

def palindromeCheck(length):
    if length == 1:
        return 32
    cnt = 0
    for row in board:
        # print(row)
        # row 안에서 몇 번 반복할지:
        for i in range(8 - length + 1):
            # 찾은 문자열 회문 검사
            temp = row[i:i+length]
            # print(temp)
            for j in range(length // 2):
                if temp[0+j] != temp[-1-j]:
                    break
            else:
                cnt += 1
    return cnt
    
# for i in range(1,9):
#     palindromeCheck(i+1)

for T in range(10):
    N = int(input())
    board = []
    for _ in range(8):
        board.append(input())
    result = 0
    result += palindromeCheck(N)
    board = list(zip(*board))
    result += palindromeCheck(N)

    print('#{0} {1}'.format(T+1, result))
