class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        # first need to get the counts
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Now add add the num to respective index in bucket array
        # each index reps the count num and the array of that index
        # is the frequency of the count
        for num_key in count.keys():
            buckets[count[num_key]].append(num_key)

        ans = []

        for bucket in buckets[::-1]:
            for num in bucket:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans