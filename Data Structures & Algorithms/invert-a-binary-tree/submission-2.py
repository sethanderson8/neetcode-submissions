# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS, first we visit the node
        # base csae is if None, return
        # then we swap its left and right
        self.invert_tree_helper(root)
        return root

    def invert_tree_helper(self, node):
        # base case
        if node is None:
            return
        # process - flipping left and right
        temp = node.left
        node.left = node.right
        node.right = temp
        # dfs its children
        self.invert_tree_helper(node.left)
        self.invert_tree_helper(node.right)