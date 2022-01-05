# LEET CODE 24 Swap Node Pairs
# Given the head of a linked list, rearrange
# the list so the adjacent pairs of nodes are
# swapped . . . For example . . . 
# 1 -> 2 -> 3 -> 4 = 2 -> 1 -> 4 -> 3
import random
from ListNode import LinkedList

def swapPairs (head):
    cur = head
    while cur is not None:
        if cur.next is not None:
            tmp = cur.val
            cur.val = cur.next.val
            cur.next.val = tmp
            cur = cur.next.next
        else:
            cur = cur.next
    return head


ll = LinkedList()
for i in range(10):
    ll.add(i)
ll.show()

swapPairs(ll.head)
ll.show()

