class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key_num in freq:
            heapq.heappush(min_heap, (freq[key_num], key_num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        ans = []

        for _, num in min_heap:
            ans.append(num)

        return ans