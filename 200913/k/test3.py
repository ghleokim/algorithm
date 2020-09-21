# # compare = lambda i, q: q if q is True else i == q
# # compare_score = lambda i, q: return i >= q

# print(compare('java', 'java'))
# print(compare('java', True))
# print(compare('java', 'cpp'))


# # def solution(info, query):
# #     query_processed = []
# #     q_index = (0,2,4,6,7)

# #     for q in query:
# #         q_split = q.split(' ')
# #         q_process = [True if q_split[qi] == '-' else q_split[qi] for qi in q_index]
# #         query_processed.append(q_process)


# lang = ["java","python","cpp"]
# part = ["frontend", "backend"]
# experience = ["junior", "senior"]
# food = ["pizza", "chicken"]

# # info : "java", "backend", "junior", "pizza", "150"
# def make_index(target_dict, info, visited):
#     if all(visited):
#         return
#     else:
#         for i in range(4):
#             if visited[i] = 1: continue
#             visited[i] = 1


#             target_dict.get[]

# def get_query(info_processed, q):
#     q_split = [q[qi] for qi in q.split(' ')]

#     filter(compare)


# def solution(info, query):
#     target_dict = {}
#     info_processed = [info_item.split(' ') for info_item in info]

#     query_answer = [get_query(info_processed, q) for q in query]

#     return query_answer


# solution(
#     [
#         "java backend junior pizza 150",
#         "python frontend senior chicken 210",
#         "python frontend senior chicken 150",
#         "cpp backend senior pizza 260",
#         "java backend junior chicken 80",
#         "python backend senior chicken 50"
#     ],	
#     [
#         "java and backend and junior and pizza 100",
#         "python and frontend and senior and chicken 200",
#         "cpp and - and senior and pizza 250",
#         "- and backend and senior and - 150",
#         "- and - and - and chicken 100",
#         "- and - and - and - 150"
#     ])


# def perm(arr):
#     result = [[*arr]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             put_db([*arr])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result

def add_db(db_dict, item, score):
    if db_dict.get(item) is None:
        db_dict[item] = {"all": []}
    db_dict[item]['all'].append(score)

def update_db(db_dict, info, score, visited):
    if all(visited): return
    else:
        for i in range(4):
            if visited[i] == 1: continue
            visited[i] = 1
            add_db(db_dict, info[i], score)
            if all(visited): 
                visited[i] = 0
                continue

            update_db(db_dict[info[i]], info, score, [*visited])
            visited[i] = 0

def get_query(db_dict, query):
    cur_dict = db_dict
    for q in query:
        if q == '-': continue
        cur_dict = cur_dict.get(q)
        if cur_dict is None:
            return []
    return cur_dict['all']

def solution(info, query):
    db_dict = {"all": []}

    for info_item in info:
        info_item = info_item.split(' ')
        db_dict["all"].append(info_item[4])
        update_db(db_dict, info_item[:4], info_item[4], [0,0,0,0])
    from pprint import pprint

    pprint(db_dict)
    result = []
    for q_item in query:
        q_item = q_item.split(' ')
        q_result = get_query(db_dict, [q_item[i] for i in [0,2,4,6]])
        result.append(sum(map(lambda x: int(x) >= int(q_item[7]), q_result)))
    
    print(result)
    return result

solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ],	
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ])