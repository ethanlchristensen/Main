# LEET CODE 24 Swap Node Pairs
# Given the head of a linked list, rearrange
# the list so the adjacent pairs of nodes are
# swapped . . . For example . . . 
# 1 -> 2 -> 3 -> 4 = 2 -> 1 -> 4 -> 3

from ListNode import ListNode

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

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
head.show()
swapPairs(head)
head.show()