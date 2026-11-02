# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode()
        dummy_pointer = dummy
        counter = 0

        for ind_list in lists:
            if ind_list:
                heapq.heappush(min_heap, (ind_list.val, counter, ind_list))
                counter += 1
        
        while min_heap:
            dummy_pointer.next = heapq.heappop(min_heap)[2]
            dummy_pointer = dummy_pointer.next
            if dummy_pointer.next:
                counter += 1
                heapq.heappush(min_heap, (dummy_pointer.next.val, counter, dummy_pointer.next))

        return dummy.next
