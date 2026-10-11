class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = {}
        self.seen = set()
        self.dupes = set()
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        return next(iter(self.queue),-1)

    def add(self, value: int) -> None:
        if value in self.dupes:
            return
        elif value in self.seen:
            self.queue.pop(value)
            self.dupes.add(value)
        else:
            self.queue[value] = 1
            self.seen.add(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
