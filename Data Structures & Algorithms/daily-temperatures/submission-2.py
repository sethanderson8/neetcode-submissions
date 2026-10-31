class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while temp_stack and temp_stack[-1][0] <= temperatures[i]:
                # keep popping til you find one that is higher, otherwise
                # this is the highest and have it be 0
                temp_stack.pop()
            
            if temp_stack and temp_stack[-1][0] > temperatures[i]:
                ans[i] = temp_stack[-1][1] - i

            temp_stack.append((temperatures[i], i))

        return ans

        # [30,38,30,36,35,40,28]
        # 40,38
        # 1,4,1,2,1,0,0
