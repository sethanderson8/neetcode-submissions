class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6]
        #[1, 1,  2,  8] - left to right (prefix prod) 
        #[48, 24, 6, 1] - right to left (postfix prod)
            # these are array[i] = prefix
        # prodcut not including self at i is
            #  ltor[i] * rtol[i+1]
        ans = []
        prev_prefix = 1
        for i in range(0, len(nums)):
            ans.append(prev_prefix)
            prev_prefix = ans[-1] * nums[i]

        prev_postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * prev_postfix
            prev_postfix = prev_postfix * nums[i]

        return ans
            
            

        

        