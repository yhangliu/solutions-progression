class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_num = 1000
        while left <= right:
            mid = (left + right)// 2
            left_ele = nums[left]
            right_ele = nums[right]
            mid_ele = nums[mid]
            min_num = min(min_num, mid_ele)
            if mid_ele > left_ele and mid_ele > right_ele:
                left = mid + 1
            elif mid_ele < left_ele and mid_ele < right_ele:
                right = mid - 1
            elif mid_ele > left_ele and mid_ele < right_ele:
                right = mid - 1
            else:
                left = mid + 1

        return min_num