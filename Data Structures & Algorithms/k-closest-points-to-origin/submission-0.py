class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max_heap (length to origin, counter, [xi, yi])
        max_heap = []
        counter = 0
        for point in points:
            dist = self.get_dist(point)
            if len(max_heap) == k and dist < -max_heap[0][0]:
                heapq.heappushpop(max_heap, (-dist, counter, point))
            elif len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, counter, point))
            counter += 1

        ans = []

        while max_heap:
            ans.append(heapq.heappop(max_heap)[2])
        
        return ans



    def get_dist(self, point):
        return (point[0]**2 + point[1]**2) ** 0.5