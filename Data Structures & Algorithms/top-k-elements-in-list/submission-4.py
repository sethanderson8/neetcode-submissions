class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_to_freq = {}

        # array of arrays where each index corresponds to freq,
        # and value is an array of nums with that freq
        freq = [[] for i in range(len(nums) + 1)]

        # getting the val to freq
        for num in nums:
            val_to_freq[num] = val_to_freq.get(num, 0) + 1

        # now place each num in corresponding freq index
        for num, freq_num in val_to_freq.items():
            freq[freq_num].append(num)

        # answer
        ans = []

        # iterate from front to back and append each most freq num
        # til the len of ans == k
        for nums in freq[::-1]:
            for num in nums:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return []

        

        


