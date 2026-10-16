class MyHashMap:

    def __init__(self):
        self.internal=[[] for i in range(1000)]    

    def put(self, key: int, value: int) -> None:
        n=key%1000
        found = False
        for pair in self.internal[n]:
            if pair[0]==key:
                found = True
                if pair[1]!=value:
                    pair[1]=value
        if not found : self.internal[n].append([key,value])

    def get(self, key: int) -> int:
        n=key%1000
        for pair in self.internal[n]:
            if pair[0] == key:
                return pair[1]
        return -1   

    def remove(self, key: int) -> None:
        n=key%1000
        for i in range(len(self.internal[n])):
            if self.internal[n][i][0] == key:
                self.internal[n].remove([key,self.internal[n][i][1]])
                break

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)