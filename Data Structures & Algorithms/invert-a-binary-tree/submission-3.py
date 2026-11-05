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
        # base case
        if root is None:
            return
        # process - flipping left and right
        temp = root.left
        root.left = root.right
        root.right = temp
        # dfs its children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root