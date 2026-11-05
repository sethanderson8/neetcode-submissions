class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [2,-1,1,2]
        # 2,1,2,4
        # hash map of seen sums with count
        # iterate over each sum, if its compliment to equal k is in
        # the hash map, add that count to the ans
        # regardless, always update the freq of the sum just seen
        past_prefix_sum = 0
        prefix_sum = []
        sum_freqs = {past_prefix_sum: 1}
        total_subarrays = 0
        for num in nums:
            # find what the cur prefix is
            cur_prefix_sum = past_prefix_sum + num
            # add that to the prefix_sum array
            prefix_sum.append(cur_prefix_sum)
            # find the compliment needed for equal k
            compliment = cur_prefix_sum - k
            # check if it has been seen already and += the count of it here
            if compliment in sum_freqs:
                total_subarrays += sum_freqs[compliment]
            # update the count of the current prefix sum in our sum freq
            sum_freqs[cur_prefix_sum] = sum_freqs.get(cur_prefix_sum, 0) + 1
            # update the past_prefix_sum with our current one
            past_prefix_sum = cur_prefix_sum

        return total_subarrays
