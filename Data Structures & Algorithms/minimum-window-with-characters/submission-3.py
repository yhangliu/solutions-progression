class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        s_counts = defaultdict(int)
        left = 0
        min_len = float("inf")
        ans = ''

        if len(t) > len(s):
            return ''
        
        while left < len(s) and s[left] not in t:
            left += 1
        for right in range(left, len(s)):

            curr_char = s[right]
            if curr_char in t_counts:
                s_counts[curr_char] += 1
                if s_counts[curr_char] > t_counts[curr_char]:
                    left_char = s[left]
                    if left_char in t:
                        while s_counts[s[left]] > t_counts[s[left]]:
                            s_counts[s[left]] -= 1
                            left += 1
                            while left <= len(s) and s[left] not in t:
                                left += 1                                     
            matches = 0
            for key in t_counts:
                if t_counts[key] <= s_counts[key]:
                    matches += 1
            
            if matches == len(t_counts):
                if right - left + 1 < min_len:
                    min_len =  right - left + 1
                    ans = s[left: right + 1]

        return ans
                

        