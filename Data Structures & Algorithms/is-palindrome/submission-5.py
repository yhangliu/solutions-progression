class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        if len(s) == 0 or len(s) == 1:
            return True
        left = 0
        right = len(s) - 1
        while left <= len(s)-1 and not s[left].isalnum():
            left += 1
        while not s[right].isalnum() and right >= 0:
            right -= 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1
            
        return True