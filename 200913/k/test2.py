def add_count(s_choice, count_orders):
    if count_orders.get(s_choice) is None:
        count_orders[s_choice] = 0
    count_orders[s_choice] += 1
    return

def combination(order, c, choice, visited, count_orders):
    n = len(order)

    if len(choice) == c:
        add_count(''.join(choice), count_orders)
        return

    else:
        for i in range(n):
            if visited[i]: continue
            new_choice = [*choice]
            new_choice.append(order[i])
            visited[i] = 1
            combination(order,c, new_choice,[*visited], count_orders)

def solution(orders, course):
    count_orders = {}
    
    for order in orders:
        for number in course:

            combination(sorted(order), number, [], [0 for _ in range(len(order))], count_orders)

    print(count_orders)

    max_counts = [0 for _ in range(len(course))]
    max_results = [[] for _ in range(len(course))]


    for res_order in count_orders.keys():
        course_index = course.index(len(res_order))
        res_order_count = count_orders[res_order]
        if max_counts[course_index] > res_order_count: continue
        elif max_counts[course_index] == res_order_count:
            max_results[course_index].append(res_order)
        else:
            max_counts[course_index] = res_order_count
            max_results[course_index] = [res_order]
        
    answer = []

    for i in range(len(course)):
        if max_counts[i] > 1:
            answer.extend(max_results[i])

    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]	)
solution(["XYZ", "XWY", "WXA"],	[2,3,4])