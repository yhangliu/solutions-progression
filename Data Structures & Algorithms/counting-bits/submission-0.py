class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            counts = Counter(bin(num))
            ans.append(counts["1"])
        return ans