class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = 1000

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            ans = min(ans, num)
            if num < nums[right]:
                right = mid -1
            else:
                left = mid + 1
        

        return ans