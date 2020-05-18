user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]

def compare():
    return True










# 조합
n = 5
r = 2

def generate(n, r, visited, start=0, chosen=[]):
    if len(chosen) == r:
        # print(chosen)
        return
    else:
        for i in range(start, n):
            if visited[i]: continue
            chosen.append(i)
            visited[i] = 1
            generate(n, r, visited, start+1, chosen)
            visited[i] = 0
            chosen.pop()



visited = [0 for i in range(n)]

generate(5,3, visited)