import sys
sys.setrecursionlimit(int(1e5))

string_to_index = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index_to_string = alphabet.split()

for i in range(26):
    string_to_index[alphabet[i]] = i

class Trie:
    def __init__(self):
        self.children = [0 for _ in range(26)]
        self.is_terminal = False
        self.count = 0
        return

    def insert(self, key):
        current = self
        for k in key:
            current.count += 1
            index = string_to_index[key[0]]
            current.children[index] = Trie()
            current = current.children[index]

        current.is_terminal = True
        return

    def find(self, key):
        current = self
        for k in key:
            if k == '?':
                return current.count
            elif current.is_terminal:
                return current.count
            else:
                index = string_to_index[k]
                current = current.children[index]
                if current == 0: return 0

def solution(words, queries):
    max_length = max(map(len, queries))
    
    trie_front = [Trie() for _ in range(max_length+1)]
    trie_back = [Trie() for _ in range(max_length+1)]
    
    for word in words:
        trie_front[len(word)].insert(word)
        trie_back[len(word)].insert(word[::-1])

    answer = []
    queried = {}

    for query in queries:
        # hashing from dictionary
        former_answer =  queried.get(query)
        if former_answer:
            count = former_answer

        elif query[0] == '?':
            count = trie_back[len(query)].find(query[::-1])
            queried[query] = count
        else:
            count = trie_front[len(query)].find(query)
            queried[query] = count

        answer.append(count)
    
    return answer


res = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(res)