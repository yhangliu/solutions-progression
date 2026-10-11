class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            char = s[right]

            while char in seen:
                left_char = s[left]
                seen.remove(left_char)
                left += 1
            seen.add(char)
            ans = max(ans, right - left + 1)
        return ans


        