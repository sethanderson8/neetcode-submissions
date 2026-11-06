# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque([(root, 0)])
        while queue:
            level_len = len(queue)
            # Each level reset the leftmost and rightmost
            leftmost_node_ind = queue[0][1]
            rightmost_node_ind = queue[0][1]
            for i in range(level_len):
                cur_node, cur_ind = queue.popleft()
                rightmost_node_ind = max(rightmost_node_ind, cur_ind)
                cur_width = (rightmost_node_ind - leftmost_node_ind) + 1
                max_width = max(max_width, cur_width)
                # process children
                if cur_node.left:
                    queue.append((cur_node.left, 2 * cur_ind))
                if cur_node.right:
                    queue.append((cur_node.right, 2 * cur_ind + 1))

        return max_width
