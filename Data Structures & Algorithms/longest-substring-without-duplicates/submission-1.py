class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        counts = defaultdict(int)
        max_len = 0

        for right in range(n):
            right_char = s[right]
            counts[right_char] += 1
            while counts[right_char] > 1:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
        