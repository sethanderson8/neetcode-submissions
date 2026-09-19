class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Use HashMap to collect values and freqs
        # Use a maxHeap and go through all elements in map and add them to max heap 
        # as a KV pair where k is value and v is frequency
        # O(n + k) - Space
        # O(n * log(k)) - Time

        freqs = {}
        maxHeap = []

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        # Code for adding KV pair to heap!!
        for key in freqs.keys():
            # Negative for max heap
            heapq.heappush(maxHeap, (-freqs.get(key), key))

        topKMostFrequent = []

        for i in range(k):
            topKMostFrequent.append(heapq.heappop(maxHeap)[1])

        return topKMostFrequent