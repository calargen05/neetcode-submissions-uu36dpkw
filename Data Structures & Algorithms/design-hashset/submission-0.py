class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)
            return

    def remove(self, key: int) -> None:
        if key in self.hashset:
            count = 0
            for i in range(len(self.hashset)):
                if self.hashset[i] == key:
                    count = i
                    break
            
            self.hashset.pop(count)
            return

    def contains(self, key: int) -> bool:
        return key in self.hashset
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)