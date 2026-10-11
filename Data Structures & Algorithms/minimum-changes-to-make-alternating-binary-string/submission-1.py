class Solution:
    def minOperations(self, s: str) -> int:
        prev = s[0]
        changes = 0
        for char in s[1:]:
            if prev == char:
                changes += 1
                if char == '1':
                    prev = '0'
                else:
                    prev = '1'
            else:
                prev = char
        

        return min(changes, len(s) - changes)