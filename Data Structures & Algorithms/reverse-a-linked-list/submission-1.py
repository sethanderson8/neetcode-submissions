# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        pointerNode = head
        nextNode = head
        while pointerNode is not None:
            nextNode = pointerNode.next
            pointerNode.next = prevNode
            prevNode = pointerNode
            pointerNode = nextNode

        return prevNode