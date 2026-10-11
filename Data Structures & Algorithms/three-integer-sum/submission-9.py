class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)

        result = []
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < n and nums[j - 1] == nums[j]:
                        j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return result
