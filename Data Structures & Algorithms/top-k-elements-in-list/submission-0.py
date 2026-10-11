class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_counts = len(nums) * [0]
        num_counts = Counter(nums)
        n = len(nums)

        for i in range(n):
            count_counts[i] = []

        for key, value in num_counts.items():
            count_counts[value-1].append(key)
        ans = []
        for i in range(n-1, -1, -1):
            for count in count_counts[i]:
                if len(ans) < k:
                    ans.append(count) 
        return ans