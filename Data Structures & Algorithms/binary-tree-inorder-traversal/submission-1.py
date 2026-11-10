# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversed = []
        self.traverse_helper(root, traversed)
        return traversed

    def traverse_helper(self, root, traversed):
        if root: # if root is not none basically enter
            #left
            self.traverse_helper(root.left, traversed)
            #self
            traversed.append(root.val)
            #right
            self.traverse_helper(root.right, traversed)
            