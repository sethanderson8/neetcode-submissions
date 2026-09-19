# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.levelOrderHelper(root, res, 1)

        return res

    def levelOrderHelper(self, root, res, depth):
        if root is not None:
            print(root.val)
            if len(res) < depth:
                res.append([root.val])
            else:
                res[depth - 1].append(root.val)

            self.levelOrderHelper(root.left, res, depth + 1)
            self.levelOrderHelper(root.right, res, depth + 1)