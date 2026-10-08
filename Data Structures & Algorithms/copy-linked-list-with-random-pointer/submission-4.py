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
        node_list_original_to_copy = defaultdict(lambda: Node(0))
        node_list_original_to_copy[None] = None

        cur_pointer = head

        while cur_pointer:
            node_list_original_to_copy[cur_pointer].val = cur_pointer.val
            node_list_original_to_copy[cur_pointer].next = node_list_original_to_copy[cur_pointer.next]
            node_list_original_to_copy[cur_pointer].random = node_list_original_to_copy[cur_pointer.random]
            cur_pointer = cur_pointer.next

        return node_list_original_to_copy[head]


        