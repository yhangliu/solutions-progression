class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cheapest = float("inf")

        ans = 0

        for price in prices:
            ans = max(ans, price - cheapest)
            cheapest = min(cheapest,price)

        return ans