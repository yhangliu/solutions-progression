class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_val = nums[0]


        while left <= right:
            mid = (left + right)//2
            min_val = min(min_val, nums[mid])
            if nums[mid] <= nums[right]:
                right = mid - 1
            else: 
                left = mid + 1

        return min_val
            
        