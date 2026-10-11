class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        curr_sum = nums[0]
        max_sum = nums[0]
        for right in range(1, len(nums)):
            num = nums[right]
            curr_sum += num
            if num > curr_sum:
                curr_sum = num

            max_sum = max(max_sum, curr_sum)
        return max_sum

