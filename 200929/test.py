"""
01 
"""
def solution(S):
    # write your code in Python 3.6
    answer = 0
    N = len(S)
    i = 0
    consecutive_a = 0
    has_substring_aaa = False
    
    while i < N:
        
        if S[i] == 'a':
            consecutive_a += 1
        else:
            answer += 2 - consecutive_a
            consecutive_a = 0
        
        if consecutive_a == 3:
            return -1
        
        i += 1
    
    answer += 2 - consecutive_a
        
    return answer


"""
02
"""

def solution(S):
    # write your code in Python 3.6
    # answer : [ indexes in S of string beloning pair-1, pair-2, index of char in string ]
    answer = []
    N = len(S)
    M = len(S[0])
    
    NUM_ALPHABET = 26
    ORD_A = ord('a')
    
    alphabet_indexes = [ [ [] for _ in range(M) ] for __ in range(NUM_ALPHABET)]
    
    for ni in range(N):
        given_string = S[ni]
        
        for mi in range(M):
            alphabet_i = ord(given_string[mi]) - ORD_A
            
            if len(alphabet_indexes[alphabet_i][mi]) == 0:
                alphabet_indexes[alphabet_i][mi].append(ni)
            else:
                previous_ni = alphabet_indexes[alphabet_i][mi][0]
                answer = [previous_ni, ni, mi]
                return answer
    
    return answer

"""
Q3
"""

def solution(A):
    # write your code in Python 3.6
    answer = 0
    
    N = len(A)
    counts = [0 for _ in range(N)]
    
    changable_number = []
    
    for i in range(N):
        target_index = A[i] - 1
        
        if counts[target_index] == 0:
            counts[target_index] += 1
        else:
            changable_number.append(target_index)
            
    changable_number.sort()
    
    ci = 0
    
    for i in range(N):
        if counts[i] == 1: continue
        
        answer += abs(changable_number[ci] - i)
        ci += 1
    
    return answer