# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB

        # they will eventually meet up as we progress one by one, either at the
        # intersection or at None
        while pointer_a != pointer_b:
            # since not the same, lets progress both
            # pointer_a goes to the next node or to headB, if none
            if pointer_a:
                pointer_a = pointer_a.next
            else:
                pointer_a = headB

            # pointer_b goes to the next node or to headA, if none
            if pointer_b:
                pointer_b = pointer_b.next
            else:
                pointer_b = headA

        return pointer_a
        