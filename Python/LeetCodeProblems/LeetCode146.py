# LEET CODE 146 LRU Cache
class LRUCache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = 0
        self.most_recent = None
        self.cache = {}
        

    def get(self, key):
        if key in self.cache:
            self.most_recent = key
            return self.cache[key]
        

    def put(self, key, value):
        if self.entries < self.capacity:
            self.cache[key] = value
            self.entries += 1
            return True
        else:
            print("CACHE FULL")
            return False

my_cache = LRUCache(2)
for i in range(5):
    if my_cache.put(i, i):
        print((i,i), "inserted into the cache . . .")
    else:
        print("FAILED TO INSERT", (i,i), "into the cache . . .")