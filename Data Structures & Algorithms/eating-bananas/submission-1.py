class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        min_k = float('inf')

        while left <= right:
            mid = (left + right) // 2
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile/mid)
            
            #Eating too slow, search for faster rate
            if time_to_eat > h:
                left = mid +1
            else:
                min_k = min(min_k, mid)
                right = mid -1
        return min_k
        