"""
기초 아이디어: 소팅하는 방법
1. 입력값을 숫자로 일대일 맵핑한다.
    if strcmp(inp, 'ZRO')
    ...
2. 이후 정렬한다.
3. 정렬된 숫자를 str로 일대일 맵핑한다.

기초 +1: 카운팅 소트 사용

"""

p = ['ZRO ', 'ONE ', 'TWO ', 'THR ', 'FOR ', 'FIV ', 'SIX ', 'SVN ', 'EGT ', 'NIN ']

def getidx(num):
    for i in range(10):
        if num[0] == p[i][0] and num[1] == p[i][1] and num[2] == p[i][2]:
            return i
for T in range(int(input())):

    temp = input()
    nums = input().split()

    cnt = [0] * 10

    for num in nums:
        cnt[getidx(num)] += 1

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    print('#{0} {1}'.format(T+1, ans))

"""
공간을 팔아서 시간을 번다.
100 * 100 
#0.18838s
"""
numidx = [[0] * 100 for _ in range(100)]
numidx[ord('Z')][ord('R')] = 0
numidx[ord('O')][ord('N')] = 1
numidx[ord('T')][ord('W')] = 2
numidx[ord('T')][ord('H')] = 3
numidx[ord('F')][ord('O')] = 4
numidx[ord('F')][ord('I')] = 5
numidx[ord('S')][ord('I')] = 6
numidx[ord('S')][ord('V')] = 7
numidx[ord('E')][ord('G')] = 8
numidx[ord('N')][ord('I')] = 9

p = ['ZRO ', 'ONE ', 'TWO ', 'THR ', 'FOR ', 'FIV ', 'SIX ', 'SVN ', 'EGT ', 'NIN ']

for T in range(int(input())):
    temp = input()
    nums = input().split()

    cnt = [0] * 10

    for num in nums:
        cnt[numidx[ord(num[0])][ord(num[1])]] += 1

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    print('#{0} {1}'.format(T+1, ans))

"""
"""

numidx = [[0] * 100 for _ in range(100)]
numidx[ord('T')][ord('W')] = 2
numidx[ord('T')][ord('H')] = 3
numidx[ord('F')][ord('O')] = 4
numidx[ord('F')][ord('I')] = 5
numidx[ord('S')][ord('I')] = 6
numidx[ord('S')][ord('V')] = 7

numidx[ord('Z')][ord('R')] = 0
numidx[ord('O')][ord('N')] = 1
numidx[ord('E')][ord('G')] = 8
numidx[ord('N')][ord('I')] = 9

num1 = [0] * 100
num1[ord('Z')] = 1
num1[ord('O')] = 2
num1[ord('E')] = 9
num1[ord('N')] = 10

num1[ord('T')] = 0
num1[ord('F')] = 0
num1[ord('S')] = 0




p = ['ZRO ', 'ONE ', 'TWO ', 'THR ', 'FOR ', 'FIV ', 'SIX ', 'SVN ', 'EGT ', 'NIN ']

for T in range(int(input())):
    temp = input()
    nums = input().split()

    cnt = [0] * 10

    for num in nums:
        a = num1[ord(num[0])]
        if a:
            cnt[a-1] += 1
        else:
            cnt[numidx[ord(num[0])][ord(num[1])]] += 1

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    print('#{0} {1}'.format(T+1, ans))