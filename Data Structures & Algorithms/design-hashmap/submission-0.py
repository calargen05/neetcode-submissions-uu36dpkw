class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        included = 0

        for kv in self.hashmap:
            if key == kv[0]:
                included = 1
                break

        if included:
            for kv in self.hashmap:
                if kv[0] == key:
                    kv[1] = value
                    return
        else:
            self.hashmap.append([key,value])

    def get(self, key: int) -> int:
        for kv in self.hashmap:
            if key == kv[0]:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        val = 0
        for kv in self.hashmap:
            if kv[0] == key:
                val = kv[1]
                self.hashmap.remove([key,val])
                return
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)