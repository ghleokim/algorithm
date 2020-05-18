# N = 5

# s = [1,2,3,4,5]

# visited = [0,0,0,0,0]
# for i in range(N):
#     visited[i] = 1
#     for j in range(N):
#         if visited[j]: continue
#         print(s[i], s[j])

""""""
 
# a = [0,1,2,3,4,5,6]

# print(a[:3] + [0] + a[3:])


a = [2,3,4,5,6]

a = []

print(a[:-1])


"""
def define_dir(dir_dict, path):
    cur = dir_dict
    
    for d in path[:-1]:
        cur = cur[d]
    
    cur[path[-1]] = {}
    
    return

def mkdir(arg=''):
    print('mkdir')

def rm(arg=''):
    print('')

def solution(directory, command):
    answer = []
    dir_dict = {'/': {}}
    
    # construct dictionary first
    for path in directory[1:]:
        if path == '/': continue
        path_li = path.split('/')
        define_dir(dir_dict, path_li[1:])

    # print(dir_dict)
    
    command_dict = {'mkdir': mkdir, }
    c_li = command[0].split()
    
    command_dict[c_li[0]](c_li[1])
    
    return answer
"""


s = [ ["ACCOUNT2", "150"], ["ACCOUNT1", "100"],  ["ACCOUNT100", "150"]]

s.sort(key=lambda x: x[0])

print(s)

"""4

def withdraw(target, amount, snapshots):
    for i in range(len(snapshots)):
        if target == snapshots[i][0]:
            changed_amount = int(snapshots[i][1]) - int(amount)
            snapshots[i][1] = str(changed_amount)
            break
        else:
            continue
    return    

def save(target, amount, snapshots):
    found = False
    for i in range(len(snapshots)):
        if target == snapshots[i][0]:
            found = True
            changed_amount = int(snapshots[i][1]) + int(amount)
            snapshots[i][1] = str(changed_amount)
            break
        else:
            continue
            
    if not found:
        snapshots.append([target, amount])
        
    return    

def solution(snapshots, transactions):
    answer = [[]]
    transaction_history = [0 for i in range(100001)]
    
    for transaction in transactions:
        t_id = int(transaction[0])
        if transaction_history[t_id]:
            continue
        else:
            # visit
            transaction_history[t_id] = 1
            
            action, target, amount = transaction[1:]
            
            if action == 'SAVE':
                save(target, amount, snapshots)
            else:
                withdraw(target, amount, snapshots)
        
    snapshots.sort(key=lambda x: x[0])
    
    return snapshots
"""


'''
def get_len(road, i):
    count = 0
    length = 0
    
    while True:
        length += len(road[i])
        if road[i] == '':
            length += 1
            count += 1
        i += 1
        
        if i == len(road):
            return length
        if count == 3:
            break
        
    return length

def solution(road, n):
    answer = -1
    road = road.split('0')
    
    
    for i in range(len(road)):
        cur_max = get_len(road, i)
        answer = max(answer, cur_max)
    
    return answer
'''
"""3
def get_len(road, i, n):
    count = 0
    length = 0
    
    while True:
        length += len(road[i])
        if road[i] == '':
            length += 1
            count += 1
        i += 1
        # end
        if i == len(road):
            break
        if count == n:
            length += len(road[i])
            break
        
    return length

def solution(road, n):
    answer = -1
    road = road.split('0')
    
    
    for i in range(len(road)):
        cur_max = get_len(road, i, n)
        answer = max(answer, cur_max)
    
    return answer
"""