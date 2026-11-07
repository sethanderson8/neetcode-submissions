# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre order - self, c1, c1c1 (None), c1c2 (None), c2, c2c1(None), c2c2
        # in order - c1c1(None), c1, c1c2(None) self, c2c1(none), c2, c2c2  

        # pre order - the root is always the first element
        # in order, we find the root there, all elements to the left of it are one the left half
        # of the root, all elements to the right of it are to the right side of the root
        # After finding the index of the root in the in order we can use that index to find the
        # len of nodes to left of it and the len of nodes to the right of it
        # We can then use the preorder array and those two len vals (left_of_root_len and right_of_root_len)
        # to actually
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        pre_idx = 0
        return self.buildTreeHelper(preorder, pre_idx, 0, len(inorder) - 1, inorder_map)


    def buildTreeHelper(self, preorder: List[int], pre_idx, in_left: int, in_right: int, inorder_map) -> Optional[TreeNode]:
        # Base case, when there is no vals, we are the smallest we can split
        if in_left > in_right:
            return None

        root_val = preorder[pre_idx]
        root_in_order_ind = inorder_map[root_val]
        current_node = TreeNode(root_val)

        # How many nodes are in the left subtree?
        left_len = root_in_order_ind - in_left
        
        # Left starts at pre_idx + 1
        current_node.left = self.buildTreeHelper(preorder, pre_idx + 1, in_left, root_in_order_ind - 1, inorder_map)
        # Right skips over the root (+1) AND all left subtree nodes (+left_len)
        current_node.right = self.buildTreeHelper(preorder, pre_idx + 1 + left_len, root_in_order_ind + 1, in_right, inorder_map)

        return current_node