

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_counter = Counter(s)

        for i, char in enumerate(s):
            if char_counter[char] == 1:
                return i
        return -1