"""
1 <= n <= 200
weak의 길이 1 이상 15 이하


"""
def permutation(arr):
    length = len(arr)
    candidate = list(set(arr))
    count = [arr.count(i) for i in range(100)]

    result = []

    for first in candidate:
        stack = []
        new_count = [*count]

        new_count[first] -= 1
        stack.append([[first], new_count])

        while stack:
            top, top_count = stack.pop()
            # print(top, top_count)

            if len(top) == length:
                result.append(top)
                continue

            for c in candidate:
                if top_count[c] > 0:
                    new_top_count = [*top_count]
                    new_top_count[c] -= 1
                    item = [[*top, c], new_top_count]
                    stack.append(item)
            
    return result

def fix(n, weak, start, perm, direction):
    weak_mod = weak[start:] + [w + n for w in weak[:start]]
    dist_mod = [weak_mod[i+1] - weak_mod[i] for i in range(len(weak))][::direction]
    
    # print('in')
    count = 0
    left = 0
    right = 1

    for p in perm:
        # print(weak_mod, dist_mod, p, left, right)
        if left > len(weak)-1:
            return count
            break
        elif p < dist_mod[left]:
            count = -1
            return -1
            break
        else:
            count += 1
            while p >= sum(dist_mod[left:right]):
                right += 1
                if right > len(weak):
                    break
            
            left = right
            right = left + 1

    return count

                
    
    
    

def solution(n, weak, dist):
    answer = -1
    if len(weak) == 1:
        return 1

    for direction in (-1, 1):
        for w in range(len(weak)):
            for item in permutation(dist):
                res = fix(n, weak, w, item, direction)
                if answer == -1:
                    answer = res
                elif res != -1:
                    answer = min(res, answer)

    return answer

if __name__ == "__main__":
    n = 12
    weak = [1, 3, 4, 9, 10] # [1,5,6,10]
    dist = [3, 5, 7] # [1,2,3,4]
    result = 1

    # print(solution(n, weak, dist))
    # print(permutation([1,3,3,1]))

    print(solution(n,weak,dist))
    print(solution(12,[1,5,6,10], [3,5,7]))

    # print(solution(50, [0], [6]))
    # print(solution(200, [0,10,50,80,120,160], [1,10,5,40,30]))


"""
테스트 1 〉	통과 (1.01ms, 10.7MB)
테스트 2 〉	통과 (0.95ms, 10.8MB)
테스트 3 〉	통과 (4449.42ms, 16.7MB)
테스트 4 〉	통과 (3937.86ms, 16.8MB)
테스트 5 〉	통과 (0.46ms, 10.8MB)
테스트 6 〉	통과 (49.64ms, 10.7MB)
테스트 7 〉	통과 (0.30ms, 10.8MB)
테스트 8 〉	통과 (1.16ms, 10.6MB)
테스트 9 〉	통과 (2.01ms, 10.7MB)
테스트 10 〉	통과 (1169.25ms, 11.6MB)
테스트 11 〉	통과 (613.91ms, 11.1MB)
                        테스트 12 〉	실패 (7030.82ms, 16.7MB)
테스트 13 〉	통과 (548.36ms, 11.1MB)
                        테스트 14 〉	실패 (1736.29ms, 11.8MB)
테스트 15 〉	통과 (3951.26ms, 13.5MB)
                        테스트 16 〉	실패 (시간 초과)
테스트 17 〉	통과 (9166.91ms, 16.8MB)
테스트 18 〉	통과 (9569.31ms, 16.7MB)
                        테스트 19 〉	실패 (시간 초과)
테스트 20 〉	통과 (5579.54ms, 13.5MB)
                        테스트 21 〉	실패 (시간 초과)
테스트 22 〉	통과 (2.80ms, 10.7MB)
                        테스트 23 〉	실패 (1.57ms, 10.8MB)
테스트 24 〉	통과 (2.67ms, 10.8MB)
                        테스트 25 〉	실패 (0.46ms, 10.7MB)
"""