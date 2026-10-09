class Solution:
    def isHappy(self, n: int) -> bool:
        cur_num = n
        next_num = 0
        seen_nums = set()

        while cur_num != 1:
            prev_num = cur_num
            while prev_num > 0:
                single_digit = prev_num % 10
                prev_num = prev_num // 10
                next_num += (single_digit * single_digit)
            cur_num = next_num
            next_num = 0
            if cur_num in seen_nums:
                return False
            else:
                seen_nums.add(cur_num)
                
        return True
        