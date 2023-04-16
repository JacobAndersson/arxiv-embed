class MemoryCache():
    def __init__(self, size):
        self.cache = {}
        self.size = size

    def get(self, key):
        return self.cache.get(key, None)

    def set(self, key, value):
        if len(self.cache) >= self.size:
            self.cache.popitem()
        self.cache[key] = value
