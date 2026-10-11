class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        max_consec = 0
        for num in seen:
            consec = 0
            if num - 1 not in seen:
                while(num in seen):
                    num += 1
                    consec += 1
            max_consec = max(max_consec, consec)

        return max_consec