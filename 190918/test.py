# 
"""
numArr = [
    [None, 9   , 0   , None],
    [1   , 2   , None, None],
    [None, 4   , None, 6   ],
    [5   , 7   , 3   , 8   ]
]

numArr2 = ['' for _ in range(2**6)]

numList = ['1101', '11001', '10011', '111101', '100011', '110001', '101111', '111011', '110111', '1011']
for idx, num in enumerate(numList):
    numArr2[int(num, base=2)] = idx

print(numArr2)

string = '1110110110001011101101100010110001000110100100110111011'

s1 = f'{string:0>56}'
print(s1)

s2 = '0' * (56-len(string)) + string
print(s2)

print(set(string))

s3 = 0

string2 = '0000011101101100010111011011000101100010001101001001101110110000000000'

for i in range(len(string2)-1,-1,-1):
    if string2[i] == '1':
        s3 = string2[i-55:i+1]
        break

print(s3)
print(int('11', base=2))

for i in range(8):
    print(numArr[int(s3[i*7+1:i*7+3], base=2)][int(s3[i*7+4:i*7+6], base=2)], end=' ')
    print(numArr2[int(s3[i*7:(i+1)*7], base=2)])
"""
# text = '0123456789ABCDEF'
# for hexnum in text:
#     if hexnum.isdigit():
#         binnum = bin(ord(hexnum)-48)
#     else:
#         binnum = bin(ord(hexnum)-65+10)
#     print(binnum)


# 16진수 to 2진수

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

print([*map(ord, ('0','1','9','A','F'))])

text = '196EBC5A316C578'
newtext = ''.join([f'{bin(int(t,base=16))[2:]:0>4}' for t in text])
print(len(newtext))

res = []

text = '00001F8E3F1FF1F80381F81C7E00E00E3F1C7FF8E00FC188D6E2DDBB6E34'

index = len(text) - 1
stack = ''
k = 1
found = False

while index >= 0:
    print('stack', len(stack), stack, 'text', text[index])
    # 거꾸로 탐색
    # 시작 전 0 걸러내기
    if not stack and text[index] == '0': 
        index -= 1
        continue

    # 첫 번째로 만나는 hex값에서 0 떼고 가져오기
    elif not stack and text[index]:
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
        if len(stack) >= 7 * k:
            tmp = stack[-7*k:]
            print('k', k, 'tmp', tmp)
            if k == 1:
                if tmp in numDict.keys():
                    found = True
                else:
                    k += 1
            else:
                for j in range(7):
                    print(j, len(tmp), k, tmp[j*k:(j+1)*k], set(tmp[j*k:(j+1)*k]))
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
            print('add tmp', tmp)
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
            res.append([k, ''.join([stack[-56*k:][__] for __ in range(0,56*k,k)])])
            stack = ''
            k = 1
            found = False
            index -= 1

print(res)





# newtext = [f'{bin(int(t,base=16))[2:]:0>4}' for t in text]
# print(newtext)
# newtext = ''.join(newtext)
# newtext = newtext.strip('0')
# print(len(newtext),newtext)
# print(f'{newtext:0>112}')
# for i in range(8):
#     print(' ',2*i*7,2*(i+1)*7,' ')
#     print(f'{newtext:0>112}'[2*i*7:2*(i+1)*7], end='')
# print()

# text = '000000000000000000000000000196EBC5A316C57800000000'
# print(text.split('0'))

# print([int(t,base=2) for t in textB.split()])
