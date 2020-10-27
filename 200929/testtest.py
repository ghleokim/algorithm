def solution(A):
    # write your code in Python 3.6
    answer = 0
    LARGE_NUM = 1000000000
    
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

        if answer > LARGE_NUM:
            return -1
    
    return answer

A = [1 for _ in range(44722)]

print(solution(A))