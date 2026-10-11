class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(step, subset):
            if step >= len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[step])
            dfs(step + 1, subset)

            subset.pop()
            while step + 1 < len(nums) and nums[step] == nums[step+1]:
                step += 1
            dfs(step + 1, subset)
        dfs(0, [])
        return ans
        