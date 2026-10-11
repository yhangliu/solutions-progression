class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        stack = []
        stack.append(intervals[0])
        for i in range(1, len(intervals)):
            prev_start, prev_end = stack[-1]
            curr_start, curr_end = intervals[i]
            if curr_start <= prev_end:
                stack[-1] = [prev_start, max(prev_end,curr_end)]
            else:
                stack.append(intervals[i])

        return stack