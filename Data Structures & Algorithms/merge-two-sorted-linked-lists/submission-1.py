# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyPointer = dummyNode
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                dummyPointer.next = list1
                list1 = list1.next
            else:
                dummyPointer.next = list2
                list2 = list2.next
            dummyPointer = dummyPointer.next

        if list1 is None:
            dummyPointer.next = list2
        else:
            dummyPointer.next = list1

        return dummyNode.next