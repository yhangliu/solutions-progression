class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left <= right:
            left_height = heights[left]
            right_height = heights[right]
            max_height = min(left_height, right_height)
            length = right - left
            area = max_height * length
            max_area = max(area, max_area)
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area
        