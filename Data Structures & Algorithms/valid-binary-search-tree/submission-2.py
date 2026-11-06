# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return (self.is_valid_bst_helper(root, math.inf, -math.inf))

    def is_valid_bst_helper(self, node, less_val, great_val):
        if not node:
            # if none, we return true since that the end
            return True
        is_cur_node_valid = node.val < less_val and node.val > great_val
        # left side need to be less than the cur nodes val
        left_side_valid = self.is_valid_bst_helper(node.left, node.val, great_val)
        right_side_valid = self.is_valid_bst_helper(node.right, less_val, node.val)

        return is_cur_node_valid and left_side_valid and right_side_valid
        