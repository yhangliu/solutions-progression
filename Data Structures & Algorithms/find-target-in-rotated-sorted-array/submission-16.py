class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)// 2
            num = nums[mid]
            if num == target:
                return mid
            elif num >= nums[left]:
                if target >= nums[left] and target <= num:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= num and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1