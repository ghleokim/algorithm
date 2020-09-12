# 후보 키
# https://programmers.co.kr/learn/courses/30/lessons/42890

from pprint import pprint

def concatenate(string_array):
    return ''.join([f'{s:_<8}' for s in string_array])

def combination(array):
    n = len(array)
    res = []
    for i in range(1, 2**n):
        turn = []
        for j in range(n):
            if i & (1<<j): turn.append(array[j])
        yield (i, turn)

def compare(a, b):
    # 겹치지 않으면 None
    # 겹치면 더 큰 결과를 리턴
    if a|b == a:
        return a
    elif a|b == b:
        return b

    return None

def make_index(row, combination_dict_array, is_possible_array):
    for index, row_combination in combination(row):
        if is_possible_array[index] == 0: continue
        current = concatenate(row_combination)

        if combination_dict_array[index].get(current) is None:
            combination_dict_array[index][current] = 1
        else:
            is_possible_array[index] = 0
            combination_dict_array[index][current] += 1

def check_possible(is_possible_array):
    for i in range(len(is_possible_array)):
        for j in range(len(is_possible_array)):
            if i == j: continue
            elif all([is_possible_array[i],is_possible_array[j]]):
                compare_result = compare(i,j)
                if compare_result == None: continue
                else:
                    is_possible_array[compare_result] = 0
            else:
                continue
    
    return sum(is_possible_array)

def solution(relation):
    if len(relation[0]) == 1: return 1

    combination_dict_array = [{} for _ in range(2 ** len(relation[0]))]
    is_possible_array = [1 for _ in range(2 ** len(relation[0]))]
    is_possible_array[0] = 0

    for row in relation:
        make_index(row, combination_dict_array, is_possible_array)

    # pprint(combination_dict_array)
    print(is_possible_array)

    result = check_possible(is_possible_array)
    print(is_possible_array)

    return result

# solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])


# solution([["10000000","ryan","music","2"]])
# print(solution([["10000000"]]))
# print(solution([["a","aa"],["aa","a"],["a","a"]]))

print(concatenate(["10000000","ryan","music","2"]))

"0000","0123"
"00000""123"