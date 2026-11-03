class MedianFinder:
    # use two heaps, a min heap and a max heap that splits the list
    # of vals in half.
    # Will need to rebalance each time you add a num to make sure it is evenly split
        # Rebalance each time the two heaps differ by more than 1

    # Then for find median, if the two heaps are equal size, you return the avg between the two
    # if not equal you just return the top of the larger heap

    def __init__(self):
        # upper half [4,5,6]
        self.min_heap = []
        # lower half [1,2,3]
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        # Route strictly against max_heap's top
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)


        while abs(len(self.min_heap) - len(self.max_heap)) >= 2:
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            else:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        

        #max: -1, -3
        #min:  2
        #