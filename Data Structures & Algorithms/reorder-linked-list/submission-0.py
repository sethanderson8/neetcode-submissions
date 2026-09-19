# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # start at beginning of list
        # create pointer for that spot
        # move pointer until it is end of list, chop prev.next and insert in spot
        # move to next val
        
        curPointer = head
        while curPointer:
            prevNode = curPointer
            swapNode = curPointer
            while swapNode.next:
                prevNode = swapNode
                swapNode = swapNode.next
            prevNode.next = None
            curNextNode = curPointer.next # None
            curPointer.next = swapNode
            swapNode.next = curNextNode #None
            curPointer = curNextNode
# [0, 1, 2, 3, 4, 5, 6]
# [0, 6, 1, 5, 2, 4, 3]