class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for day in range(n):
            while stack and temperatures[day] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day] = day - prev_day
            stack.append(day)
        return ans