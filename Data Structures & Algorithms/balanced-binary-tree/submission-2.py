# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced_helper(root) != -1

    def is_balanced_helper(self, root):
        if root is None:
            return 0

        # first we need to DFS the children
        left_subtree_height = self.is_balanced_helper(root.left)
        right_subtree_height = self.is_balanced_helper(root.right)

        # Then we will check for imbalance
        if (left_subtree_height == -1 or right_subtree_height == -1 or 
            abs(left_subtree_height - right_subtree_height) > 1):
            return -1

        return max(left_subtree_height, right_subtree_height) + 1

        