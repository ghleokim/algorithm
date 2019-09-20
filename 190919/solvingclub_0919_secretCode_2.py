def hex2bin(hexnum):
    if hexnum.isdigit():
        num = ord(hexnum) - 48
    else:
        num = ord(hexnum) - 55
    # print(hexnum, 'is', num)
    res = ''
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return f'{res:0>4}' if res else '0000'


def rowsearch(row, n):
    global M, indexboard
    index = M*4-1
    found = False
    k = 1
    stack = ''
    while index >= 0:
        # if stack: print(index, stack)
        current = row[index]
        if not stack and current == '0':
            index -= 1; continue
        elif not stack and current == '1':
            start = index
            formerend = indexboard[n-1][start]
            if formerend is not None:
                if row[formerend:start+1] == binboard[n-1][formerend:start+1]:
                    indexboard[n][start] = formerend
                    index = formerend - 1
                    continue
            stack += current
        elif not found and len(stack) == k * 7:
            for _ in range(7): # 14: 01 23 45 67 89
                # print(k, stack, set(stack[_*k:_*(k+1)]), _*k,_*(k+1))
                if len(set(stack[k*_:k*(_+1)])) != 1:
                    k += 1
                    break
            else:
                comp = ''.join([stack[j*k]for j in range(7)])
                if comp in numDict.keys():
                    found = True
                else:
                    k += 1
            stack += current
        elif found and len(stack) == k * 56:
            chunk = ''.join([stack[j*k] for j in range(56)])
            result.append(((k ,n, index),chunk))
            indexboard[n][start] = index
            k = 1
            found = False
            stack = ''
        else:
            stack += current
        index -= 1
    return 0


def checkValid(num):
    try:
        res = [numDict[num[i*7:(i+1)*7]] for i in range(8)]
        # print('success:', T, r, en, num)
    except:
        print('error:', T, r, en, num)
        sys.exit()
    tmpSum = sum(res)
    checkSum = 2 * (res[1] + res[3] + res[5] + res[7]) + tmpSum
    if checkSum % 10:
        return 0
    else:
        return tmpSum

# sample_text = '01E06079861E79F99FE079861E79F800000000000000000000'
# rows = []
# row = ''
# for t in sample_text:
#     row += hex2bin(t)

import sys
sys.stdin = open('input/input.txt')

numDict = {
    '1011000':0,
    '1001100':1,
    '1100100':2,
    '1011110':3,
    '1100010':4,
    '1000110':5,
    '1111010':6,
    '1101110':7,
    '1110110':8,
    '1101000':9
}


for T in range(int(input())):
    N, M = map(int,input().split())

    hexboard = []

    for i in range(N):
        hexboard.append(input())

    binboard = []

    for row in hexboard:
        temprow = ''
        for r in row:
            temprow += hex2bin(r)
        binboard.append(temprow)

    # from pprint import pprint   
    # pprint(hexboard)
    # pprint(binboard)

    result = []
    results = 0

    indexboard = [[None for _ in range(M*4)] for __ in range(N)]

    for n, row in enumerate(binboard):
        rowsearch(row, n)

    # print(result)
    for en, r in enumerate(result):
        results += checkValid(r[1])

    print(results)


# text = '11011100001100010001110111101110110000111101110111010000'
# checkValid(text)