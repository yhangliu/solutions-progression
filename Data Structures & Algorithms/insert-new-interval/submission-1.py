class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals) - 1
        target = newInterval[0]

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        intervals.insert(left, newInterval)

        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            prev_start, prev_end = stack[-1]
            curr_start, curr_end = interval
            if curr_start <= prev_end:
                stack[-1] = [prev_start, max(prev_end, curr_end)]
            else:
                stack.append(interval)

        return stack
        