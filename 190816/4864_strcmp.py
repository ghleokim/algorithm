import sys
sys.stdin = open('input/input_4864.txt')

# 방법1: 0.15924s
for T in range(int(input())):
    str1, str2 = input(), input()
    result = 0    
    if str1 in str2:
        result = 1
    print('#{0} {1}'.format(T+1, result))

# 방법2: 0.15216s
for T in range(int(input())):
    str1, str2 = input(), input()
    result = 0    
    for i in range(len(str2)-len(str1)+1):
        for idx in range(len(str1)):
            strtmp = str2[i+len(str1)-idx-1]
            if strtmp != str1[-idx-1]:
                break
        else:
            result = 1
            break
        
        for j in range(1, len(str1)):
            if strtmp[-1] == str1[-j-1]:
                i += j
                break
        else:
            i += 1
    

    print('#{0} {1}'.format(T+1, result))