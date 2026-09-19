# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curNode = root
        self.invertTreeHelper(curNode)

        return root
        
    def invertTreeHelper(self, curNode):
        if curNode is not None:
            tempLeft = curNode.left
            curNode.left = curNode.right
            curNode.right = tempLeft
            self.invertTreeHelper(curNode.right)
            self.invertTreeHelper(curNode.left)