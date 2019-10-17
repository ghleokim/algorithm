arr = [
    [1,2,3],[4,5,6],[7,8,9]
]

arr2 = [arr,arr,arr]
print(arr2)

a = []
for i in arr:
    a.extend(i)

b = [i for sub in arr for i in sub]

c = [i for sub in arr2 for s in sub for i in s]

print(a, b, c)


# queue
class Q():
    data=[]

    def enQ(self, n):
        self.data.append(n)
    
    def deQ(self, n):
        x = self.data[0]
        del self.data[0]
        return x
