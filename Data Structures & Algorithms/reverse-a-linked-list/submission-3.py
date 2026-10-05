# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseListHelper(self, cur_node: Optional[ListNode], prev_node: Optional[ListNode]):
        if cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            return self.reverseListHelper(next_node, cur_node)
        else:
            return prev_node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListHelper(head, None)
        