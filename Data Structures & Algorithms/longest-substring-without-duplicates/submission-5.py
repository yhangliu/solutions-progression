class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        longest = 0

        counts = defaultdict(int)
        for i in range(len(s)):
            char = s[i]
            counts[char] += 1
            while counts[char] > 1:
                counts[s[left]] -= 1
                left += 1
            longest = max(longest, i - left + 1)
        return longest
