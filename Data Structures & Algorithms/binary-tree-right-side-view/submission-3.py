# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # we essentially only want to pull the val of the right most node
        # per each level
        # how to figure if right most, it will be the last node at that depth
        # in the queue, if we change depth, we know the right most of the depth
        # depth is the node directly preceeding the node of the new depth
        # could also use a hash map of depth to queue and have a counter to increment depth
        # and iterate over it. When a given depth queue is at len(1) and only has one node in
        # it, we know that node is the right most
        # When no nodes left in queue at cur depth, go to next depth
        if not root:
            return []

        ans = []
        cur_depth = 1
        # default will be a deque
        depth_to_queue = defaultdict(deque, {cur_depth: deque([root])})

        while depth_to_queue[cur_depth]:
            cur_queue = depth_to_queue[cur_depth]
            cur_node = cur_queue.popleft()
            
            # add children at deeper depth
            if cur_node.left:
                depth_to_queue[cur_depth + 1].append(cur_node.left)
            if cur_node.right:
                depth_to_queue[cur_depth + 1].append(cur_node.right)

            # Only after adding their children at the correct depth, do we check if we are
            # processing the last node of a given depth
            if not cur_queue:
                ans.append(cur_node.val)
                cur_depth += 1

        return ans
            

        