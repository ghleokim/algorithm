def solution(numbers):
    answer = {}

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j: continue
            exists = answer.get(numbers[i]+numbers[j])

            if exists is None:
                answer[numbers[i]+numbers[j]] = 1

    return list(answer.keys()).sort()