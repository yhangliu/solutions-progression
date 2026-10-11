class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            diff = abs(x-y)
            if diff != 0:
                heapq.heappush(stones, -diff)
        if stones:
            return -1 * stones[0]
        return 0
        