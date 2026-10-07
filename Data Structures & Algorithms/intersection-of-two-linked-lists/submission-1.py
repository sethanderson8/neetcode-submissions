# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hash Set solution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()

        pointer_a = headA
        while pointer_a:
            node_set.add(pointer_a)
            pointer_a = pointer_a.next

        pointer_b = headB
        while pointer_b:
            if pointer_b in node_set:
                return pointer_b
            else:
                pointer_b = pointer_b.next

        return pointer_b
            
        