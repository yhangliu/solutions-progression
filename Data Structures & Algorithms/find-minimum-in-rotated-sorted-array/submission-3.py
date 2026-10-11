class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while left <= right:
            mid = (left + right)//2
            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            if nums[0] <= nums[mid] and nums[-1] <= nums[mid]:
                left = mid +1
            elif nums[0] >= nums[mid] and nums[-1] >= nums[mid]:
                right = mid - 1
            else:
                return nums[0]
        return nums[0]
            
        