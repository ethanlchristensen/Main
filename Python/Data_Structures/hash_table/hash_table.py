import sys
sys.path.append('/Data_Structures/linked_list')

from linked_list import linked_list

class hash_table:
    def __init__(self, MAX):
        self.MAX = MAX
        self.arr = [linked_list.linked_list() for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        flag = False
        h = self.get_hash(key)
        for i in range(self.MAX):
            l = self.arr[i]
            if l.dup_check(val):
                flag = True
        if not flag:
            self.arr[h].push(val)
        
    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]
    
    def __delitem__(self, key):
        self.arr[self.get_hash(key)] = None
        
    def print_hash(self):
        print('HASH TABLE')
        print('POS LINKED LIST')
        for i in range(self.MAX):
            print('{}: '.format(i), end = ' ')
            self.arr[i].display()
            
            