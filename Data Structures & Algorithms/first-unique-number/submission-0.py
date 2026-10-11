class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counts = defaultdict(int)
        self.q = nums
        for num in nums:
            self.counts[num] += 1
        

    def showFirstUnique(self) -> int:
        for num in self.q:
            if self.counts[num] == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.counts[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
