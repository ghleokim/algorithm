import sys
sys.setrecursionlimit(int(1e5))

string_to_index = lambda s: ord(s)-97
index_to_string = lambda i: chr(i+97)

class Trie:
    def __init__(self):
        self.children = [0 for _ in range(26)]
        self.is_terminal = False
        self.count = 0
        return

    def insert(self, key):
        self.count += 1
        index = string_to_index(key[0])
        if self.children[index] == 0:
            self.children[index] = Trie()
        if len(key) == 1: return
        
        self.children[index].insert(key[1:])

        return

    def find(self, key):
        if key[0] == '?':
            return self.count
        else:
            index = string_to_index(key[0])
            if (self.children[index]) == 0:
                return 0
            return self.children[index].find(key[1:])

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