# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Queue of nodes of size n
        # [1,2,3,4,5,6,7,8,9] n = 3
        # [1], [1,2], [1,2,3], [2,3,4], [3,4,5]......[6,7,8,9] [7,8,9]
        # Each time you pop, that is the prev_node_n_away 6...
        # Once you get to end, you remove 7, reattach the prev_node_n_away to 8, and return head
        prev_node_n_away = None
        curPointer = head

        # Make sure to restrict to size n!
        node_queue = deque()
        while curPointer:
            node_queue.append(curPointer)
            if len(node_queue) > n:
                prev_node_n_away = node_queue.popleft()
            curPointer = curPointer.next

        if prev_node_n_away:
            deleted_node = node_queue.popleft()
            # Just grab the node that comes after the deleted one
            prev_node_n_away.next = deleted_node.next
            return head
        else:
            # here we are deleting cases where we simply delete the first index of this linked list
            return head.next

        return head




        