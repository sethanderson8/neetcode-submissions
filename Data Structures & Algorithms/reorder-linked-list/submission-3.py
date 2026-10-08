# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Efficient way - fast and slow pointer
        # Use this to find the center point of the linked list first pass
        # the slow pointer will be the mid point to start the interleaving

        fast = head.next
        mid = head
        # find mid point
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        # reverse the second half
        second_half_pointer = mid.next
        mid.next = None # split the halves
        prev_node = None
        while second_half_pointer:
            next_node = second_half_pointer.next
            second_half_pointer.next = prev_node
            prev_node = second_half_pointer
            second_half_pointer = next_node

        first_half_pointer = head
        second_half_pointer = prev_node

        # interleave them
        while second_half_pointer and first_half_pointer:
            first_half_next = first_half_pointer.next
            second_half_next = second_half_pointer.next
            first_half_pointer.next = second_half_pointer
            second_half_pointer.next = first_half_next
            first_half_pointer = first_half_next
            second_half_pointer = second_half_next
            
        
        

        

