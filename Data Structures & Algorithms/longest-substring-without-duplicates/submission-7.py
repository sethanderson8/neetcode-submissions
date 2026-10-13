class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to check for uniques
        # when unique, add to set and increment cur_max
        # Always check and update cur_max with total_max
        # When dupe is found, we move left_pointer removing from
        # set and decrementing cur_max until we have reached the last occured
        # right char + 1. Once we have reached there with left pointer, we
        # continue moving right char til end of string
        
        left = 0
        right = 0
        unique_chars = set()
        cur_max = 0
        total_max = 0

        while right < len(s):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
                cur_max -= 1
            unique_chars.add(s[right])
            cur_max += 1
            total_max = max(cur_max, total_max)
            right += 1

        return total_max

        # "zxyzxyz"
        #   l        
        #     r      
        # unique_chars = (x,y,z)
        # cur_max = 3
        # total_max = 3