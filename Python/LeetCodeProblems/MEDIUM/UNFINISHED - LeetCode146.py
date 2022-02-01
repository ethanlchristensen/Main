# LEET CODE 146 LRU Cache
class LRUCache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = 0
        self.most_recent = None
        self.cache = {}
        

    def get(self, key):
        self.age()
        if key in self.cache:
            self.most_recent = key
            return self.cache[key]
        

    def put(self, key, value):
        self.age()
        if self.entries < self.capacity:
            self.cache[key] = [value, 0]
            self.entries += 1
            return key in self.cache
    
    def age(self):
        print("we are in the age function")
        if len(self.cache) != 0:
            for k in self.cache:
                self.cache[k][1] += 1
    
            

my_cache = LRUCache(2)
for i in range(5):
    print(my_cache.cache)
    if my_cache.put(i, i):
        print((i,i), "inserted into the cache . . .")
        my_cache.get(i)
    else:
        print("FAILED TO INSERT", (i,i), "into the cache . . .")