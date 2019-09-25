#BFS
from pprint import pprint

start = [20, 21, 23]
end = [20, 23, 24]


i = len(start)-2
cur = [i+1]

while i > 0:
    if start[i] == start[cur[::-1][-1]]:

    i -= 1