class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        min_val = nums[0]
        min_idx = 0
        while left <= right:
            mid = (left + right) // 2
            if min_val > nums[mid]:
                    min_val = nums[mid]
                    min_idx = mid
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        if target > nums[min_idx] and target <= nums[-1]:
            left = min_idx
            right = len(nums) - 1
        else:
            left = 0
            right = min_idx

        while left <= right:
            mid = ((left + right)) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
                
            
        