
# 인접행렬

person = [None for _ in range(101)]

# DFS, queue
L, S = map(int, input().split())
c = [*map(int, input().split())]

for i in range(L//2):
    if not person[c[2*i]]:
        person[c[2*i]] = [c[2*i+1]]
    else:
        person[c[2*i]].append(c[2*i+1])

visited = [0 for _ in range(101)]

queue = [person[S]]
visited[S] = 1
max_person = S

while queue:
    per = queue[0]
    del queue[0]

    for p in per:
        if not visited[p]:
            if p > max_person:
                max_person = p
            visited[p] = 1
            if person[p]:
                queue.append(person[p])
    
print(visited)
print(max_person)
