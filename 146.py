class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.length = capacity
        self.lru_key = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_key.remove(key)
            self.lru_key.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru_key.remove(key)
            self.lru_key.append(key)
            self.cache[key] = value
            return None
        if self.length <= len(self.cache):
            k = self.lru_key.pop(0)
            self.cache.pop(k)
            self.cache[key] = value
        else:
            self.cache[key] = value
        self.lru_key.append(key)
        return None
