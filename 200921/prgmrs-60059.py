# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3

from pprint import pprint

def check_filtered_key(key):
    """
        key: 2D list
    """

    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j]: return True

    return False

def convert_to_bin(key):
    N = len(key)
    res = 0
    for i in range(N):
        for j in range(N):
            if key[i][j]: res += 1 << N*N - (i * N + j)-1
    return res

def rotate(key):
    N = len(key)
    res = [[key[i][j] for i in range(N-1,-1,-1)] for j in range(N)]
    return res

def get_key_combination(M, key):
    """
        4 방향에 대해서 모두 체크

    """
    N = len(key)
    padded_width = (M-1) * 2 + N

    res = []

    for i in range(4):
        padded_key = [[0 for _ in range(padded_width)] for __ in range(padded_width)]

        key = rotate(key)
        for ki in range(N):
            for kj in range(N):
                padded_key[M-1+ki][M-1+kj] = key[ki][kj]
    
        for si in range(padded_width - (M-1)):
            for sj in range(padded_width - (M-1)):
                cur_key = [[padded_key[si+ki][sj+kj] for kj in range(M)] for ki in range(M)]
                bin_cur_key = convert_to_bin(cur_key)
                if bin_cur_key:
                    if bin_cur_key not in res:
                        res.append(bin_cur_key)

    return res

def solution(key, lock):
    M = len(lock)
    comb = get_key_combination(M, key)
    
    bin_lock = convert_to_bin(lock)

    required_key = bin_lock ^ ((1 << M**2)-1)
    if required_key == 0:
        return True
    
    return required_key in comb

res = solution([[1, 0], [0, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(res)