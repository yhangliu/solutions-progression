class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix_prod = n * [1]
        prefix_prod[0] = nums[0]
        for i in range(1,n):
            prefix_prod [i] = prefix_prod[i-1] * nums[i]

        curr_right = 1
        for j in range(n-1,0,-1):
            prefix_prod[j] = prefix_prod[j-1] * curr_right
            curr_right *= nums[j]
        prefix_prod[0] = curr_right
        return prefix_prod