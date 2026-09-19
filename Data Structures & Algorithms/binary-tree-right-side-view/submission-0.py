# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Each node need to check and see if there is a right node
        # Specifically needed to see if we need to include left node

        # Need the right most node at each depth
        # could go through all level order and replace whatever node is currently at that depth
        res = []
        self.rightSideViewHelper(root, res, 1)
        return res

    def rightSideViewHelper(self, root, res, depth):
        if root is not None:
            if len(res) < depth:
                res.append(root.val)
            else:
                res[depth - 1] = root.val

            self.rightSideViewHelper(root.left, res, depth + 1)
            self.rightSideViewHelper(root.right, res, depth + 1)