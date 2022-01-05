class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class LinkedList():
    
    def __init__(self, val = None):
        self.head = ListNode(val, None)


    def show(self):
        print("Linked List: ", end="")
        cur = self.head
        while cur is not None:
            if cur.val != None:
                print(cur.val, end=" ")
            cur = cur.next
        print()


    def add(self, val):
        cur = self.head
        if self.head.val == None:
            self.head.val = val
            return
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val, None)


    def remove(self, val):
        cur = self.head
        while cur is not None:
            if cur.val == val:
                if cur.next is not None:
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                    return
                else:
                    cur.val = None
                    return
            else:
                cur = cur.next
        print("ERROR: remove(): value", val, "is not in the Linked List.")
        

