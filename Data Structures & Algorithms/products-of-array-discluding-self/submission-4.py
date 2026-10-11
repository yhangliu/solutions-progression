class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        right_prod = 1
        prefix_prod = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        #print(prefix_prod)
        for i in range(len(nums) - 1, -1, -1):
            tmp = nums[i]
            nums[i] = prefix_prod[i] * right_prod
            right_prod *= tmp
        return nums