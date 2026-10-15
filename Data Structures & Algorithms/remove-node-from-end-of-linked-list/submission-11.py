# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        trailer = leader = dummy

        while n > 0:
            n -= 1
            leader = leader.next

        while leader.next:
            leader = leader.next
            trailer = trailer.next

        trailer.next = trailer.next.next

        return dummy.next
