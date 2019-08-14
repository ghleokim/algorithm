import sys
sys.stdin = open('input/input_4865.txt', 'r')
# str1 = 'XYPV'
# str2 = 'EOGGXYPVSY'

"""
방법1: 딕셔너리 이용
"""
"""
for T in range(int(input())):
    str1, str2 = input(), input()

    dict1 = dict.fromkeys(set(str1))

    for ch in str2:
        if ch in str1:
            if dict1[ch] is not None:
                dict1[ch] += 1
            else:
                dict1[ch] = 1

    print('#{0} {1}'.format(T+1, max(dict1.values())))
"""

"""
방법2: 
"""
for T in range(int(input())):
    str1, str2 = input(), input()
    



    print('#{0} {1}'.format(T+1, T))