# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p, q)[1]
        
    def lca(self, node, p, q):
        if node is None:
            return (False, None)
        node_is_p_or_q = node == p or node == q
        left_has_p_or_q, left_lca = self.lca(node.left, p, q)
        right_has_p_or_q, right_lca = self.lca(node.right, p, q)
        # If a deeper left or right LCA has been found, we return that right away
        if left_lca:
            return(True, left_lca)
        if right_lca:
            return(True, right_lca)
        # This is the LCA and there is no deeper (left or right LCAs)
        if node_is_p_or_q + left_has_p_or_q + right_has_p_or_q >= 2:
            return (True, node)
        
        # we return None here since this is not an LCA if has reached here
        return (node_is_p_or_q or left_has_p_or_q or right_has_p_or_q, None)