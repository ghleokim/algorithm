def solution(a):
    if len(a) == 1: return 1
    
    answer = 0
    former_direction = a[0] < a[1]

    tmp_ascending = 0

    for i in range(0, len(a)-1):
        cur_direction = a[i]<a[i+1]

        if cur_direction:
            tmp_ascending += 1
        else:
            tmp_ascending = 0
            answer += 1

        if cur_direction and not former_direction:
            answer -= 1
        
        cur_direction = former_direction

    return answer + tmp_ascending

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))