# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Unpack the final (is_balanced, height) tuple and return just the boolean  
        is_balanced, _ = self.get_height_subtree(root)
        return is_balanced

    def get_height_subtree(self, root):
        if not root:
            return (True, 0)
        
        # First DFS both children and see if those are balanced
        left_balanced, left_height = self.get_height_subtree(root.left)
        right_balanced, right_height = self.get_height_subtree(root.right)

        # Once its chilldren have been processed, now you can process this one
        cur_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        # Finally return the processing for our current node
        return (cur_balanced, 1 + max(left_height, right_height))

        


        