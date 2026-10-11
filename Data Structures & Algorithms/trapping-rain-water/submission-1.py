class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        n = len(height)
        prefix_max =  [0] * n
        suffix_max = [0] * n

        curr_max = height[0]
        for i in range(n):
            curr_max = max(curr_max, height[i])
            prefix_max[i] = curr_max
        curr_max = height[n-1]
        for i in range(n-1, -1, -1):
            curr_max = max(curr_max, height[i])
            suffix_max[i] = curr_max

        for i in range(1, n-1):
            ele = height[i]
            if prefix_max[i-1] >= ele and suffix_max[i+1] >= ele:
                print(ele)
                cap = min(prefix_max[i-1], suffix_max[i+1])
                ans += cap - ele

        return ans
