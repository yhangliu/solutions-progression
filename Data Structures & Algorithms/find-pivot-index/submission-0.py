class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = [0] * len(nums)
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_sums[i] = prefix_sum
        total = prefix_sums[-1]
        prev = 0
        for i in range(len(nums)):
            print(total - prefix_sums[i])
            print(prev)
            if (total - prefix_sums[i]) == ( prev):
                return i
            prev = prefix_sums[i]
        return -1
        