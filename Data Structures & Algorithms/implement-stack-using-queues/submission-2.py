class MyStack:

    def __init__(self):
        self.q = deque()
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        ans = None
        for _ in range(len(self.q) - 1):
            num = self.q.popleft()
            self.stack.append(num)
            ans = num
        ans = self.q.popleft()

        for _ in range(len(self.stack)):
            self.q.append(self.stack.popleft())
        return ans

        

    def top(self) -> int:
        ans = None
        for _ in range(len(self.q)):
            num = self.q.popleft()
            self.stack.append(num)
            ans = num
        

        for _ in range(len(self.stack)):
            self.q.append(self.stack.popleft())
        return ans
        

    def empty(self) -> bool:

        if self.q:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()