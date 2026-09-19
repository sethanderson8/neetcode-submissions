class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = sorted(s)
        t_sort = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(s_sort)):
            if s_sort[i] != t_sort[i]:
                return False
        
        return True