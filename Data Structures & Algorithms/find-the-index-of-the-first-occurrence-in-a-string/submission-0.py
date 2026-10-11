class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        size = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+size] == needle:
                    return i

        return -1