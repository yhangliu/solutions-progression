class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        mid = (left + right)//2


        while (left <= right):
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        return -1 