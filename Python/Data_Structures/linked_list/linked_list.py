class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
        
        
class linked_list:
    def __init__(self):
        self.head = node()
    
    def push(self,data):
        if not self.dup_check(data):
            if self.head.data == None:
                self.head = node(data)
            else:
                root = self.head
                while root.next is not None:
                    root = root.next
                root.next = node(data)
        
    def pop(self):
        if self.head == None:
            print('ERROR: List is empty, no element to pop')
            return
        else:
            root = self.head
            self.head = root.next
    
    def rm(self,index):
        if index >= self.length():
            print('ERROR: index is out of bounds')
            return
        i=0
        cur = self.head
        while True:
            prev=cur
            cur=cur.next
            if i==index:
                prev.next=cur.next
                return
            i+=1
                   
    def length(self):
        cur=self.head
        total=0
        while cur.next is not None:
            total+=1
            cur=cur.next
        return total
    
    def display(self):
        elems=[]
        cur=self.head
        while cur.next is not None:
            print('{} -> '.format(cur.data), end='')
            cur = cur.next
        if cur.data is not None:
            print(cur.data)
        else:
            print()
    
    def get(self,index):
        if index>=self.length():
            print('ERROR: index provided is out of bounds')
            return
        cur=self.head
        i=0
        while True:
            cur=cur.next
            if i==index: return cur.data
            i+=1
            
    def dup_check(self, data):
        cur = self.head
        if cur.data == None:
            return False
        while cur.next is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        if cur.data == data:
            return True
        else:
            return False
