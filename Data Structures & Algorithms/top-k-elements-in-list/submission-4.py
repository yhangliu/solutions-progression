class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        ans = []

        counts = Counter(nums)

        for key, value in counts.items():
            freqs[value].append(key)

        for freq in range(len(nums), 0, -1):
            for ele in freqs[freq]:
                ans.append(ele)
                if len(ans) == k:
                    return ans
        return ans



        