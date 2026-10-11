class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        ans = []
        for point in points:
            x,y = point
            distance = math.sqrt((x*x) + (y*y))
            heapq.heappush(heap, [distance, point])
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
        