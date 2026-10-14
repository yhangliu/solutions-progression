class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        longest = 0

        counts = set()
        for i in range(len(s)):
            char = s[i]
            while char in counts:
                to_remove = s[left]
                counts.remove(to_remove)
                left += 1
            counts.add(char)
            longest = max(longest, i - left + 1)
        return longest
"""
linear time
26 space
"""