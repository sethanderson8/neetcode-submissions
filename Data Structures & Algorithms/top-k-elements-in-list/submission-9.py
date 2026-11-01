class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) - 1
        
        for key_num in freq:
            heapq.heappush(max_heap, (freq[key_num], key_num))

        ans = []
        while k > 0:
            ans.append(heapq.heappop(max_heap)[1])
            k -= 1

        return ans