# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # search until match
        # when match search entire subtree
        # if no match, move forward with searh until match
        # repeat
        if root is None:
            return False
        
        if subRoot is None:
            return True

        if self.isSubtreeHelper(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtreeHelper(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return True and self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)
  
