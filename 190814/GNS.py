#
import sys
sys.stdin = open('input/GNS_test_input.txt', 'r')

"""
첫 번째 글자로 분류되는 숫자:
ZRO, ONT, EGT, NIN

두 번째 글자까지 접근해야 분류되는 숫자:
TWO/ THR
FOR/ FIV
SIX/ SVN
"""

"""
numStr = 'ZROONETWOTHRFORFIVSIXSVNEGTNIN'

T = int(input())
for _ in range(T):
    caseNum, numbers = input().split()
    numbers = int(numbers)

    cnt = [0] * 10

    target = input().split()

    for t in target:
        comp = t[0]

        # chr 비교로 접근
        if comp == 'Z':
            cnt[0] += 1
        elif comp == 'O':
            cnt[1] += 1
        elif comp == 'E':
            cnt[8] += 1
        elif comp == 'N':
            cnt[9] += 1
        elif comp == 'T':
            if t[1] == 'W':
                cnt[2] += 1
            else:
                cnt[3] += 1
        elif comp == 'F':
            if t[1] == 'O':
                cnt[4] += 1
            else:
                cnt[5] += 1
        elif comp == 'S':
            if t[1] == 'I':
                cnt[6] += 1
            else:
                cnt[7] += 1
        # ord로 접근

    res = []
    print(caseNum)
    for num, c in enumerate(cnt):
        n = 3 * num
        nStr = numStr[n:n+3]
        for _ in range(c-1):
            res.append(nStr)
        if num == 9:
            res.append(nStr)
        else:
            res.append(nStr)

    print(' '.join(res))
"""
# ----------------------------- #

"""[
'Z  R   O', 
'O  N   E', 
'T  W   O', 
'T  H   R', 
'F  O   R', 
'F  I   V', 
'S  I   X', 
'S  V   N', 
'E  G   T', 
'N  I   N'
]"""

"""
numStr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for _ in range(T):
    caseNum, numbers = input().split()
    numbers = int(numbers)

    cnt = [0] * 11

    target = input().split()

    for n in range(numbers):
        comp = target.pop()
        tmp = 0

        if comp == 'ZRO':
            cnt[0] += 1
        elif comp == 'ONE':
            cnt[1] += 1
            tmp = 1
        elif comp == 'TWO':
            cnt[2] += 1
            tmp = 2
        elif comp == 'THR':
            cnt[3] += 1
            tmp = 3
        elif comp == 'FOR':
            cnt[4] += 1
            tmp = 4
        elif comp == 'FIV':
            cnt[5] += 1
            tmp = 5
        elif comp == 'SIX':
            cnt[6] += 1
            tmp = 6
        elif comp == 'SVN':
            cnt[7] += 1
            tmp = 7
        elif comp == 'EGT':
            cnt[8] += 1
            tmp = 8
        else:
            cnt[9] += 1
            tmp = 9


        address = sum(cnt[:tmp-1]) * 4

        res = res[:address] + numStr[tmp] + ' ' + res[address:]

    print(caseNum)
    print(res[:-1])
"""

numStr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for _ in range(T):
    caseNum, numbers = input().split()
    numbers = int(numbers)

    cnt = [0] * 11

    target = input().split()

    targetInt = [0] * numbers

    for n in range(numbers):
        comp = target.pop()
        if comp == 'ONE':
            targetInt[n] += 1
            cnt[1] += 1
        elif comp == 'TWO':
            targetInt[n] += 2
            cnt[2] += 1
        elif comp == 'THR':
            targetInt[n] += 3
            cnt[3] += 1
        elif comp == 'FOR':
            targetInt[n] += 4
            cnt[4] += 1
        elif comp == 'FIV':
            targetInt[n] += 5
            cnt[5] += 1
        elif comp == 'SIX':
            targetInt[n] += 6
            cnt[6] += 1
        elif comp == 'SVN':
            targetInt[n] += 7
            cnt[7] += 1
        elif comp == 'EGT':
            targetInt[n] += 8
            cnt[8] += 1
        elif comp == 'NIN':
            targetInt[n] += 9
            cnt[9] += 1
        else:
            cnt[0] += 1

    countSum = [0] * 10
    for n in range(10):
        countSum[n] = countSum[n-1] + cnt[n]
    # print(cnt, countSum)

    res = ['']*numbers

    for compNum in targetInt[::-1]:
        res[countSum[compNum]-1] = numStr[compNum]
        countSum[compNum] -= 1

    # print(cnt, countSum)

    # print(cnt, countSum)
    # print(res)
    print(caseNum)
    print(' '.join(res))