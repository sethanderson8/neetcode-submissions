"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        seen_nodes_to_new_nodes = {node: Node(node.val)}

        queue = deque([node])

        while queue:
            cur_node = queue.popleft()
            cur_copied_node = seen_nodes_to_new_nodes[cur_node]
            
            for neighbor in cur_node.neighbors:
                if neighbor not in seen_nodes_to_new_nodes:
                    seen_nodes_to_new_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cur_copied_node.neighbors.append(seen_nodes_to_new_nodes[neighbor])

        return seen_nodes_to_new_nodes[node]





