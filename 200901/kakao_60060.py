#시간초과
string_to_index = lambda s: ord(s)-ord('a')
index_to_string = lambda i: chr(i + ord('a'))

class Trie:
    def __init__(self):
        self.children = [0 for _ in range(26)]
        self.is_terminal = False
        return

    def __str__(self):
        return str(self.children)

    string_exists = lambda self, key: bool(self.children[string_to_index(key)])

    def insert(self, key):
        if key == '': self.is_terminal = True
        else:
            index = string_to_index(key[0])
            if self.children[index] == 0:
                self.children[index] = Trie()
            self.children[index].insert(key[1:])

        return

    def find(self, key):
        if key == '':
            return 1 if self.is_terminal else 0 
        elif key[0] == '?':
            count = 0
            for i in range(26):
                if self.children[i] == 0: continue
                count += self.children[i].find(key[1:])
            return count
            
        else:
            index = string_to_index(key[0])
            if (self.children[index]) == 0:
                return 0
            return self.children[index].find(key[1:])

def solution(words, queries):
    trie_front = Trie()
    trie_back = Trie()
    
    for word in words:
        trie_front.insert(word)
        trie_back.insert(word[::-1])

    answer = []
    queried = {}

    for query in queries:
        # hashing from dictionary
        former_answer =  queried.get(query)
        if former_answer:
            count = former_answer

        elif query[0] == '?':
            count = trie_back.find(query[::-1])
            queried[query] = count
        else:
            count = trie_front.find(query)
            queried[query] = count

        answer.append(count)
    
    return answer

res = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(res)