# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two pointer solution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            if pointer_a:
                pointer_a = pointer_a.next
            else:
                pointer_a = headB

            if pointer_b:
                pointer_b = pointer_b.next
            else:
                pointer_b = headA

        return pointer_a