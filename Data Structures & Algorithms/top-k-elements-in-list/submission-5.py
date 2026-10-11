class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for val, count in counts.items():
            buckets[count].append(val)


        most_freq = []
        for i in range(n, -1 , -1):
            for num in buckets[i]:
                most_freq.append(num)
                if len(most_freq) == k:
                    return most_freq
        return most_freq
        