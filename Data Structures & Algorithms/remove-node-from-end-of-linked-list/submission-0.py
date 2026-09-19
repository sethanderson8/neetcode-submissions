# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leadPointer = head
        kPointer = head

        counter = 0

        while counter < n and leadPointer is not None:
            leadPointer = leadPointer.next
            counter += 1

        if leadPointer is None:
            # return value right after kPointer
            return kPointer.next

        while leadPointer.next is not None:
            leadPointer = leadPointer.next
            kPointer = kPointer.next

        kPointer.next = kPointer.next.next

        return head

        #[1,2,3,4]
        # lead: 4
        # kP: 2

        # [5]
        # lead: None
        # kP: 5
        # Breaks for this case

        # [1, 2]
        # lead: None
        # kP: 1
        #
