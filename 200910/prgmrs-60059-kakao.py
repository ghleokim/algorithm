# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

def convert_to_bit(item):
    n = len(item)
    max_length = n**2 - 1
    result = 0

    for i in range(n):
        for j in range(n):
            if item[i][j]:
                print((max_length - i*n - j))
                result += 1 << (max_length - i*n - j)

    return result

def unlock_with_key(lock, key):
    n = len(lock)
    b_lock = convert_to_bit(lock)
    b_key = convert_to_bit(key)
    print(bin(b_lock), bin(b_key), bin(b_lock | b_key), b_lock|b_key)

    if b_lock ^ b_key == 2 ** (n**2) - 1:
        return True
    
    return False

def get_key_combination(key):


    return

print(convert_to_bit([[0,0,0],[0,0,0],[0,1,1]]))


lock = [
    [1,1,1],
    [0,0,0],
    [1,1,1]
] 

key = [
    [0,0,0],
    [1,1,1],
    [0,0,0]
]

print(unlock_with_key(lock, key))