# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # width min_x == max_x = 1
        # if not 
        # max_x_per_level - min_x_per_level == max width at that level
        # each level the max and min resets
        # pass tuples to queue of the cur node and
        max_width = 1
        queue = deque([(root, 0)])
        
        while queue:
            level_len = len(queue)
            # Each level reset the min and max x
            min_x_per_level = queue[0][1]
            max_x_per_level = queue[0][1]

            for i in range(level_len):
                cur_node, cur_ind = queue.popleft()
                min_x_per_level = min(min_x_per_level, cur_ind)
                max_x_per_level = max(max_x_per_level, cur_ind)
                cur_width = (max_x_per_level - min_x_per_level) + 1
                max_width = max(max_width, cur_width)
                # process children
                if cur_node.left:
                    queue.append((cur_node.left, 2 * cur_ind +1))
                if cur_node.right:
                    queue.append((cur_node.right, 2 * cur_ind + 2))

        return max_width
