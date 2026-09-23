class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        self.mapping = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            if key in self.cache:
                self.cache.remove(key)
            elif key not in self.cache and len(self.cache) == self.capacity:
                self.cache.pop(0)
        
            self.cache.append(key)
        return self.mapping[key]
        

    def put(self, key: int, value: int) -> None:
        self.mapping[key] = value

        if key in self.cache:
            self.cache.remove(key)
        elif key not in self.cache and len(self.cache) == self.capacity:
            self.cache.pop(0)
        
        self.cache.append(key)
        

