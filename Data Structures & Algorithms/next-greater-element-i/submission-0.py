class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {}
        ans = [-1] * len(nums1)
        num_stack = []
        for i in range(len(nums1)):
            num_to_index[nums1[i]] = i

        for num in nums2:
            # Keep popping until num stack is empty and there is a top
            # value greater than it
            while num_stack and num_stack[-1] < num:
                less_than_num = num_stack.pop()
                ans[num_to_index[less_than_num]] = num
            
            # if num is in nums1 (or the num to index based on nums1),
            # we add to the stack
            if num in num_to_index:
                num_stack.append(num)

        return ans