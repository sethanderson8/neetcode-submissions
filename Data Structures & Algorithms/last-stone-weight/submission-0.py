class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            stoneX = -heapq.heappop(maxHeap)
            stoneY = -heapq.heappop(maxHeap)

            if stoneX == stoneY:
                heapq.heappush(maxHeap, 0)
            elif stoneX > stoneY:
                heapq.heappush(maxHeap, -(stoneX - stoneY))
            else:
                heapq.heappush(maxHeap, -(stoneY - stoneX))

        return -heapq.heappop(maxHeap)
