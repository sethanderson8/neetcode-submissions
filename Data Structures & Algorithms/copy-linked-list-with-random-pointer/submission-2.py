"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_list_original_to_copy = {}
        ans_head = Node(-1)

        ans_pointer = ans_head
        cur_pointer = head
        # go through entire list and get the random for each and place in corresponding index
        while cur_pointer:
            ans_pointer.next = Node(cur_pointer.val)
            ans_pointer = ans_pointer.next
            node_list_original_to_copy[cur_pointer] = ans_pointer
            cur_pointer = cur_pointer.next

        cur_pointer = head
        ans_pointer = ans_head.next

        # go through again, now anytime we see a random on the original, we will go ahead get the corresponding index of it
        # from the original list, then set the random for the ans_pointer to the corresponding node in the copy node list
        # based on the index given.
        while cur_pointer:
            if cur_pointer.random:
                ans_pointer.random = node_list_original_to_copy[cur_pointer.random]

            cur_pointer = cur_pointer.next
            ans_pointer = ans_pointer.next

        return ans_head.next

