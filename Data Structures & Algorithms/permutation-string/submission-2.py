class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        s2_counts = defaultdict(int)

        left = 0
        for right in range(len(s2)):
            char = s2[right]
            s2_counts[char] += 1

            while s2_counts[char] > s1_counts[char]:
                left_char = s2[left]
                s2_counts[left_char] -= 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False

        