import sys
sys.stdin = open('input/input.txt')

from pprint import pprint

numDict = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}

def checkValid(num):
    res = [numDict[num[i*7:(i+1)*7]] for i in range(8)]
    tmpSum = sum(res)
    checkSum = 2 * (res[0] + res[2] + res[4] + res[6]) + tmpSum
    if checkSum % 10:
        print(res,checkSum, 'invalid')
        return 0
    else:
        print(res,checkSum, 'valid')
        return tmpSum

for T in range(int(input())):
    N, M = map(int,input().split())

    board = []
    boardindex = [[None for _ in range(M)] for __ in range(N)]
    res = []
    former = [] # (startindex, endindex) tuple 저장

    for n in range(N):
        board.append(input())

    for n in range(N):
        # print(former)
        current = []
        text = board[n]
        index = len(text) - 1
        stack = ''
        k = 1
        found = False

        while index >= 0:
            # 거꾸로 탐색
            # 시작 전 0 걸러내기
            if not stack and text[index] == '0':
                index -= 1
                continue

            # 첫 번째로 만나는 hex값에서 0 떼고 가져오기
            elif not stack and text[index]:
                start = index
                above = boardindex[n-1][start]
                if above is not None:
                    boardindex[n][start] = above
                    index = above-1
                    continue
                # if former:
                #     if former[0][0] >= index:
                #         index = former[0][1]-1
                #         del former[0]
                #         # print('after delete:', index, former)
                #         continue
                hexnum = text[index]
                if hexnum.isdigit():
                    binnum = bin(ord(hexnum)-48)
                else:
                    binnum = bin(ord(hexnum)-55)
                tmp = f'{binnum[2:]:0>4}'
                i = 3
                while i > 0:
                    if tmp[i] == '0': i -= 1
                    else:
                        break
                stack += tmp[:i+1]
                index -= 1

            # 두 번째 이상:
            # 이 때는 k값을 찾았는지 못찾았는지 여부가 중요
            elif stack and not found:
                # k값 미정 - len(stack)이 7*k보다 커지기 전까지 추가
                # len(stack)이 7*k보다 크다면:
                # 1) (k가 1보다 클 경우 건너뛰기) 연속하는 k개의 숫자(ex: k=2 | 0,1 / 2,3 / 4,5 / ...)가 모두 같은지 확인
                # 2) 같다면 k가 1일 경우로 reduce: num = 001100 , k = 2 --> 010
                # 3) reduce된 숫자가 유효한 숫자이면 k값 found, 고정
                # 4) reduce된 숫자가 유효한 숫자가 아니라면 k값 not found, k += 1
                if len(stack) >= 7*k:
                    tmp = stack[-7*k:]
                    # print('k', k, 'tmp', tmp)
                    if k == 1:
                        if tmp in numDict.keys():
                            found = True
                        else:
                            k += 1
                    else:
                        for j in range(7):
                            # print(j, len(tmp), k, tmp[j*k:(j+1)*k], set(tmp[j*k:(j+1)*k]))
                            if len(set(tmp[j*k:(j+1)*k])) != 1: k += 1; break
                        else:
                            # reduce
                            tmp2 = ''.join([tmp[__] for __ in range(0,7*k,k)])
                            if tmp2 in numDict.keys():
                                found = True
                            else:
                                k += 1
                                continue
                        
                else:
                    hexnum = text[index]
                    if hexnum.isdigit():
                        binnum = bin(ord(hexnum)-48)
                    else:
                        binnum = bin(ord(hexnum)-55)
                    tmp = f'{binnum[2:]:0>4}'
                    # print('add tmp', tmp)
                    stack = tmp + stack
                    index -= 1
            elif stack and found:
                # k값 확정 - len(stack)이 56*k보다 커질 때까지 추가(숫자가 0이라도)
                if len(stack) < 56 * k:
                    hexnum = text[index]
                    if hexnum.isdigit():
                        binnum = bin(ord(hexnum)-48)
                    else:
                        binnum = bin(ord(hexnum)-55)
                    tmp = f'{binnum[2:]:0>4}'
                    stack = tmp + stack
                    index -= 1
                else:
                    res.append(''.join([stack[-56*k:][__] for __ in range(0,56*k,k)]))
                    stack = ''
                    k = 1
                    found = False
                    end = index
                    boardindex[n][start] = end
                    # current.append((start, end))
                    index -= 1
        # former = [*current]
        # print(former)
    print(res)
    result = 0

    for binText in res:
        result += checkValid(binText)
    # if T == 4:
    #     pprint(boardindex)
    print('#', end='')
    print(T+1,result)
    