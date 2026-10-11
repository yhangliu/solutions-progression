class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:
            char_array = [0] * 26
            for char in word:
                char_array[ord(char) - ord('a')] += 1
            anagrams[tuple(char_array)].append(word)
        return list(anagrams.values())
        