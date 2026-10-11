class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_counts = [[] for i in range(len(nums) + 1)]
        num_counts = Counter(nums)
        n = len(nums)


        for key, value in num_counts.items():
            count_counts[value].append(key)
        ans = []
        for i in range(n, -1, -1):
            for count in count_counts[i]:
                if len(ans) < k:
                    ans.append(count) 
        return ans