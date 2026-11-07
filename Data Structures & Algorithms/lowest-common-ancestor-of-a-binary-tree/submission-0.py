# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # you know that the root will be true
        # need to explore each subtree with dfs
        # Need to basically find the deepest tree where it is still valid (having both descendants)
        # So basically the max (True/false, depth)
        _, _, lca = self.lca_helper(root, p, q)
        return lca

    def lca_helper(self, node, p, q):
        if not node:
            return (False, False, None)

        # If itself, left-side, or right-side contains p or q, it is a valid lca
        left_p, left_q, left_lca = self.lca_helper(node.left, p, q)
        right_p, right_q, right_lca = self.lca_helper(node.right, p, q)

        # If the LCA was already found deeper in the left or right subtree, 
        # just pass it straight up without overwriting it!
        if left_lca:
            return (True, True, left_lca)
        if right_lca:
            return (True, True, right_lca)

        # Otherwise, check if THIS node is the first (deepest) one to have both p and q
        p_valid = node == p or left_p or right_p
        q_valid = node == q or left_q or right_q
        
        if p_valid and q_valid:
            return (p_valid, q_valid, node)
        return (p_valid, q_valid, None)

        


        