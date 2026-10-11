class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_counts = defaultdict(int)
        goal_counts = Counter(s1)
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            char_counts[char] += 1

            while char_counts[char] > goal_counts[char]:
                left_char = s2[left]
                left += 1
                char_counts[left_char] -= 1
            if right - left + 1 == len(s1):
                return True
        return False

        