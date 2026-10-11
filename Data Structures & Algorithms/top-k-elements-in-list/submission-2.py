class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = Counter(nums)

        ans = []
        for num, count in counts.items():
            freq[count].append(num)

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans

        