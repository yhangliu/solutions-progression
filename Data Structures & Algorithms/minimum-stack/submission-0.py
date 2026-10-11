class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            prev = self.mins[-1]
            self.mins.append(min(val,prev))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mins.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            return self.mins[-1]
        
