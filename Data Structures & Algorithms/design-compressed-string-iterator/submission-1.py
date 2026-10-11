class StringIterator:

    def __init__(self, compressedString: str):
        self.q = deque()
        i = 0
        while i < len(compressedString):
            char = compressedString[i]
            i += 1
            num = 0


            while i < len(compressedString) and compressedString[i].isdigit():
                num = num * 10 + int(compressedString[i])
                i += 1

            
            self.q.append([char, num])
        

    def next(self) -> str:
        if not self.q:
            return " "
        char, count = self.q[0]
        if count == 1:
            self.q.popleft()
        else:
            self.q[0][1] -= 1
        return char
        

    def hasNext(self) -> bool:
        if not self.q:
            return False
        return True
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
