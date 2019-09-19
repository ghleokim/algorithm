numArr = [
    [None, 9   , 0   , None],
    [1   , 2   , None, None],
    [None, 4   , None, 6   ],
    [5   , 7   , 3   , 8   ]
]
indexArr = [
    [0,1],[2,3]
]

numDict = {
    '00': {'01': 9,'10': 0},
    '01': {'00': 1,'01': 2},
    '10': {'01': 4,'11': 6},
    '11': {'00': 5,'01': 7,'10': 3,'11': 8}
}
"""
0 00110  00 10
1 01100  01 00
2 01001  01 01
3 11110  11 10  
4 10001  10 01
5 11000  11 00
6 10111  10 11
7 11101  11 01
8 11011  11 11
9 00101  00 01
"""
import sys
sys.stdin = open('input/input.txt')

"""
# 1
for t in range(int(input())):
    N, M = map(int, input().split())
    comp = ''

    for _ in range(N):
        tmp = input()
        if not comp and set(tmp) != {'0'}:
            comp = tmp

    for idx in range(len(comp)-1,-1,-1):
        if comp[idx] == '1':
            idx -= 55
            break
    
    valid, res = 0, 0

    for i in range(8):
        cur = numArr[int(comp[idx+1:idx+3],base=2)][int(comp[idx+4:idx+6],base=2)]
        idx += 7
        if i < 7:
            valid += cur * [3,1][i % 2]
            res += cur
        else:
            if (valid + cur) % 10:
                print(f'#{t+1} 0')
            else:
                print(f'#{t+1} {res+cur}')

    # digits = [numList[int(comp[i*7:(i+1)*7], base=2)] for i in range(8)]
    # print(digits)
"""

# 2
for t in range(int(input())):
    N, M = map(int, input().split())
    found = False
    for _ in range(N):
        tmp = input().strip('0')
        if not found and tmp:
            found = True
            tmp = f'{tmp:0>56}'
            odd, res, idx = 0, 0, 0
            for i in range(8):
                cur = numDict[tmp[idx+1:idx+3]][tmp[idx+4:idx+6]]
                idx += 7
                if i < 7:
                    if i % 2:
                        res += cur
                    else:
                        odd += cur
                    # valid += cur * [3,1][i % 2]
                    # res += cur
                else:
                    if (odd * 3 + res + cur) % 10:
                        print(f'#{t+1} 0')
                    else:
                        print(f'#{t+1} {odd + res + cur}')

    # digits = [numList[int(comp[i*7:(i+1)*7], base=2)] for i in range(8)]
    # print(digits)