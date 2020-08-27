"""
1 <= n <= 200
weak의 길이 1 이상 15 이하


"""
def permutation(arr):
    length = len(arr)
    candidate = list(set(arr))
    count = [arr.count(i) for i in range(length)]

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

def fix(weak, start, perm, direction):
    
    

def solution(n, weak, dist):
    answer = -1

    for direction in (-1, 1):
        for w in len(weak):
            for item in permutation(dist):
                res = fix(weak, w, item, direction)
                if res != False:
                    answer = res

    return answer

if __name__ == "__main__":
    # n = 12
    # weak = [1,5,6,10]
    # dist = [1,2,3,4]
    # result = 2

    # print(solution(n, weak, dist))
    # print(permutation([1,3,3,1]))

    print(solution(n,weak,dist))
