# bruteforce
import sys
sys.stdin = open('input/input_4861.txt', 'r')

def palindrome(inputStr):
    for i in range(len(inputStr)//2):
        if inputStr[i] != inputStr[-1-i]:
            return False
    return True

for T in range(int(input())):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input())

    found = False
    res = ''
    for row in board:
        if found:
            break
        for n in range(N-M+1):
            if palindrome(row[n:n+M]):
                res = row[n:n+M]
                found = True
                break

    # 세로탐색
    if not found:
        board = list(map(lambda x: ''.join(x), zip(*board)))
        for row in board:
            if found:
                break
            for n in range(N - M + 1):
                if palindrome(row[n:n + M]):
                    res = row[n:n + M]
                    found = True
                    break


    print('#{0} {1}'.format(T+1, res))