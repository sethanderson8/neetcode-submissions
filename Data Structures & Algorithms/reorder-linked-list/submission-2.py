# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Approach
        # curPointer
        cur_pointer = head
        while cur_pointer:
            swap_node = cur_pointer
            prev_node = cur_pointer
            while swap_node.next:
                prev_node = swap_node
                swap_node = swap_node.next
            prev_node.next = None # Prevent cycles
            cur_next_node = cur_pointer.next
            cur_pointer.next = swap_node
            swap_node.next = cur_next_node
            cur_pointer = cur_next_node



        