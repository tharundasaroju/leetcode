class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.first = None
        self.last = None
        self.length = 0

    def get(self, key: int) -> int:
        try:
            obj = self.dict[key]
            if(self.first == key):
                return obj.value
            elif(self.last == key):
                self.last = obj.after
                self.dict[obj.after].prev = None
            else:
                self.dict[obj.prev].after = obj.after
                self.dict[obj.after].prev = obj.prev
            self.dict[self.first].after = key
            obj.prev = self.first
            obj.after = None
            self.first = key
            return obj.value
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            obj = self.dict[key]
            obj.value = value
            self.get(key)
        except:
            if(self.length == 0):
                self.last = key
                self.length += 1
            elif(self.length < self.capacity):
                self.dict[self.first].after = key
                self.length += 1
            elif(self.capacity == 1):
                del self.dict[self.first]
                self.last = key
            else:
                last = self.last
                self.dict[self.dict[last].after].prev = None
                self.last = self.dict[last].after
                del self.dict[last]
                self.dict[self.first].after = key
            self.dict[key] = CacheObject(self.first, None, value)
            self.first = key

class CacheObject:
    def __init__(self, p, n, value):
        self.prev = p
        self.after = n
        self.value = value
    
    def __str__(self):
        return f"[{self.prev}, {self.after}, {self.value}]"

    def __repr__(self):
        return f"[{self.prev}, {self.after}, {self.value}]"

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)