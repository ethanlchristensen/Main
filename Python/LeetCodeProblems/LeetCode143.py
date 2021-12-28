# LEET CODE 143 REORDER LIST
# Given a sorted Linked List of the form
# L0 l1 L2 . . lN
# Reorder the list in place so it has to form 
# l0 lN l2 LN-1 L3 lN-2 . . .

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reorderList(head):

    # Find the middle of the list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the list
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # Merge the two lists
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
        


