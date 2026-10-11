class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consect = 0
        ans = 0
        for num in nums:
            if num == 1:
                consect += 1
                ans = max(ans, consect)
            else:
                consect = 0
            
        return ans