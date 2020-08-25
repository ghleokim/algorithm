"""
s = binary string consisting of  n zeros and ones

minimum number of subsequences 101010... or 010101...
두 개의 연속된 000 111 있으면 안댐

순서를 바꾸지 않고 자르거나 아닌 경우

1011101 -> 0 1 11111 0111 101 1001
not 000 101010 11100 

00110

010 01

"""

t = int(input())

for _ in range(t):
    n = int(input())
    b = input()

    arr_i = [0 for __ in range(n)]

    ends_w_zero = []
    ends_w_one = []
    
    new_sub = 1

    for i in range(n):
        if b[i] == "0":
            # b[i] == "0"
            if len(ends_w_one) == 0:
                arr_i[i] = new_sub
                ends_w_zero.append(new_sub)
                new_sub += 1
            else:
                sub = ends_w_one.pop()
                arr_i[i] = sub
                ends_w_zero.append(sub)
        else:
            # b[i] == "1"
            if len(ends_w_zero) == 0:
                arr_i[i] = new_sub
                ends_w_one.append(new_sub)
                new_sub += 1
            else:
                sub = ends_w_zero.pop()
                arr_i[i] = sub
                ends_w_one.append(sub)
    
    print(new_sub-1)
    print(' '.join([*map(str, arr_i)]))