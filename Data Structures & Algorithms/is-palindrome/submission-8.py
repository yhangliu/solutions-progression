class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()

        print(s[left].isalpha())
        while left < len(s)  and not s[left].isalnum():
            left += 1 
        while right >= 0 and not s[right].isalnum():
            right -= 1 
        while left < right:
            left_char = s[left]
            right_char = s[right]

            if left_char != right_char:
                return False
            left += 1
            right -= 1
            while not s[left].isalnum():
                left += 1 
            while not s[right].isalnum():
                right -= 1 
        return True