class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        self.head = ListNode()
        self.tail = ListNode()
        self.curr.next = self.tail
        self.curr.prev = self.head
        self.head.next = self.curr
        self.tail.prev = self.curr
        

    def visit(self, url: str) -> None:
        target = ListNode(url)
        target.prev = self.curr
        self.curr.next = target
        self.curr = self.curr.next
        self.curr.next = self.tail
        self.tail.prev = self.curr
        

    def back(self, steps: int) -> str:

        for i in range(steps):
            self.curr = self.curr.prev
            if self.curr == self.head:
                self.curr = self.curr.next
                return self.curr.val
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            self.curr = self.curr.next
            if self.curr == self.tail:
                self.curr = self.curr.prev
                return self.curr.val
        return self.curr.val
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)