class MyHashSet:

    def __init__(self):
        self.listbucket=[[] for i in range(1000)]

    def add(self, key: int) -> None:
        if key not in self.listbucket[key%1000]:
            self.listbucket[key%1000].append(key)
        
    def remove(self, key: int) -> None:
        if key in self.listbucket[key%1000]:
            self.listbucket[key%1000].remove(key)
        
    def contains(self, key: int) -> bool:
        if key in self.listbucket[key%1000]:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)