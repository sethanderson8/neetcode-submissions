# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans_node = None
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            # Here both are not None, we go iterate
            if list1.val < list2.val:
                ans_node = list1
                list1 = list1.next
            else:
                ans_node = list2
                list2 = list2.next

            ans_node_pointer = ans_node

            while list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    ans_node_pointer.next = list1
                    list1 = list1.next
                else:
                    ans_node_pointer.next = list2
                    list2 = list2.next
                ans_node_pointer = ans_node_pointer.next

            if list1 is not None:
                ans_node_pointer.next = list1
            else:
                ans_node_pointer.next = list2

        return ans_node