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

def get_query(db_dict, query, score):
    cur_dict = db_dict
    for q in query:
        if q == '-': continue
        cur_dict = cur_dict.get(q)
        if cur_dict is None:
            return 0
    
    return sum(map(lambda x: int(x) >= int(score), cur_dict['all']))

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
        q_result = get_query(db_dict, [q_item[i] for i in [0,2,4,6]], q_item[7])
        result.append(q_result)
    
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