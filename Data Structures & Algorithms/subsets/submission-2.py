import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def dfs(step):
            if step == len(nums):
                ans.append(copy.copy(path))
                return
            path.append(nums[step])
            dfs(step + 1)

            path.pop()
            dfs(step + 1)
        dfs(0)
        return ans
        