# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_the_one = False
        ans = ListNode()
        ans_pointer = ans
        l2_pointer = l2
        l1_pointer = l1
        
        while l1_pointer or l2_pointer or carry_the_one:
            ans_pointer.next = ListNode()
            ans_pointer = ans_pointer.next

            node_val = 0
            if carry_the_one:
                node_val += 1
                carry_the_one = False

            if l1_pointer:
                node_val += l1_pointer.val
                l1_pointer = l1_pointer.next

            if l2_pointer:
                node_val += l2_pointer.val
                l2_pointer = l2_pointer.next

            if node_val >= 10:
                carry_the_one = True
                node_val = node_val % 10

            ans_pointer.val = node_val
        
        return ans.next