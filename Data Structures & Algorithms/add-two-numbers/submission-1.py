# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryTheOne = False
        ans = ListNode(0)
        ansPointer = ans

        while l1 is not None or l2 is not None or carryTheOne:
            ansPointer.next = ListNode(0)
            ansPointer = ansPointer.next
            l1Digit = 0
            l2Digit = 0
            if l1 is not None:
                l1Digit = l1.val
            if l2 is not None:
                l2Digit = l2.val

            if carryTheOne:
                l2Digit += 1
                carryTheOne = False

            curAddition = l1Digit + l2Digit
            if curAddition >= 10:
                carryTheOne = True

            curAddition = (curAddition % 10)

            ansPointer.val = curAddition

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        return ans.next