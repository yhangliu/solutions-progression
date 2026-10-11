class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 1
        while left <= right:
            curr_speed = (left + right) // 2

            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile / curr_speed)
            if time_to_eat > h:
                left = curr_speed + 1
            else:
                ans = curr_speed
                right = curr_speed - 1
                
        
        return ans