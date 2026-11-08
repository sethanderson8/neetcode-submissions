# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
            
        return self.build_tree_helper(preorder, inorder, inorder_map, 0, 0, len(inorder) - 1)

    def build_tree_helper(self, preorder, inorder, inorder_map, pre_ind, left, right):
        if pre_ind >= len(preorder) or left > right:
            return None
        
        inord_ind = inorder_map[preorder[pre_ind]]
        left_tree_size = inord_ind - left
        
        cur_node = TreeNode(preorder[pre_ind])
        # Left preorder_ind will be the next val if withtin range
        cur_node.left = self.build_tree_helper(preorder, inorder, inorder_map, pre_ind + 1, left, inord_ind - 1)
        # need to also add left subtree size to the right to get the proper preord_ind for the right
        cur_node.right = self.build_tree_helper(preorder, inorder, inorder_map, pre_ind + left_tree_size + 1, inord_ind + 1, right)

        return cur_node
