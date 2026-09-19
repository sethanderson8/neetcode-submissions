class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        minHeap = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq.keys():
            heapq.heappush(minHeap, (freq[num], num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []

        while len(minHeap) > 0:
            res.insert(0, heapq.heappop(minHeap)[1])
        
        return res