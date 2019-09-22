# N자리 16진수 into N*4자리 2진수
def d2b(num):
    res = ''
    while num > 1:
        res = str(num % 2) + res
        num = num // 2
    return str(num) + res

def h2b(digit):
    if digit.isdigit():
        return d2b(ord(digit) - 48)
    else:
        return d2b(ord(digit) - 55)


for T in range(int(input())):
    N, hexNum = input().split()
    result = ''
    for h in hexNum:
        result += '{0:0>4}'.format(h2b(h))
    print('#', end='')
    print(T+1, result)

# # check
# for i in '0123456789ABCDEF':
#     print(h2b(i))

