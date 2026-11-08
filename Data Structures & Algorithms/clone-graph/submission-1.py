"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if node is None just return None
        if not node:
            return None

        seen_nodes_to_new_nodes = {}
        return self.clone_graph_helper(node, seen_nodes_to_new_nodes)

    def clone_graph_helper(self, node, seen_nodes_to_new_nodes):
        # create new copied node with just the val
        copied_node = Node(node.val)

        # add copied node to map. should be allowed since just using mem id for the key
        seen_nodes_to_new_nodes[node] = copied_node

        # list for the copied neighbors
        copied_neighbors = []
        for neighbor in node.neighbors:
            # if the neighbor has already been seen, no need to explore it again and create another
            # just use the map to add it as a neighbor directly
            if neighbor in seen_nodes_to_new_nodes:
                copied_neighbors.append(seen_nodes_to_new_nodes[neighbor])
            else:
                # if not seen before, we got to explore it and create it
                copied_neighbors.append(self.clone_graph_helper(neighbor, seen_nodes_to_new_nodes))
        
        # add the copied neighbors to the copied node
        copied_node.neighbors = copied_neighbors

        return copied_node

        