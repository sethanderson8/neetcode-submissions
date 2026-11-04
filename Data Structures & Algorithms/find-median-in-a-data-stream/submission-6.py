class MedianFinder:

    def __init__(self):
        self.min_heap = [] # upper/larger half
        self.max_heap = [] # lower/smaller half
        

    def addNum(self, num: int) -> None:
        # we will push num to the max heap, pop the largest, and push the largest from the lower half
        # to the upper half
        largest_of_lower = -heapq.heappushpop(self.max_heap, -num)
        heapq.heappush(self.min_heap, largest_of_lower)

        # if min heap now has more elements, move its smallest back to max heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2 

        
        