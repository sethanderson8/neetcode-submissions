# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        trailer = leader = dummy

        # Move trailer n nodes ahead of trailer
        while n > 0:
            leader = leader.next
            n -= 1
        
        # We then move the trailer and leader together and stop when the leader
        # is on the very last node. Specifically, beacause we need to stop the trailer
        # on the one before the one we remove.
        while leader.next:
            leader = leader.next
            trailer = trailer.next

        # Now we remove the nth node
        trailer.next = trailer.next.next

        # We now return dummy.next since we may be removing the head
        return dummy.next


        # -1,1,2,3,4,5,6,7. n = 4
        # dmt, 
        # Space them out 4 apart. We do not want the trailer to land on the node
        # we are removing but instead the prev node before so that we can properly
        # remove it
        # -1,1,2,3,4,5,6,7
        # -1,1,2,3,4,5,6,7
