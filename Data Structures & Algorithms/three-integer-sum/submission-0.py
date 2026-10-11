class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        n = len(nums)
        seen = set()
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    if (nums[i], nums[j], nums[k]) not in seen:               
                        seen.add((nums[i], nums[j], nums[k]))
                        ans.append([nums[i], nums[j], nums[k]])
                if total > 0:
                    k -= 1
                else:
                    j += 1
        return ans
        