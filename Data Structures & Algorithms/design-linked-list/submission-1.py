class ListNode:

    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    
        

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
            if curr == self.tail:
                return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        curr_head = self.head.next
        new_head = ListNode(val)
        curr_head.prev = new_head
        new_head.prev = self.head
        new_head.next = curr_head
        self.head.next = new_head
        

    def addAtTail(self, val: int) -> None:
        curr_tail = self.tail.prev
        new_tail = ListNode(val)
        self.tail.prev = new_tail
        new_tail.prev = curr_tail
        new_tail.next = self.tail
        curr_tail.next = new_tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        slow = self.head
        fast = self.head.next
        new_node = ListNode(val)
        for i in range(index):
            slow = slow.next
            fast = fast.next
            if slow == self.tail:
                return
        slow.next = new_node
        new_node.next = fast
        fast.prev = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for i in range(index):
            curr = curr.next
            if curr == self.tail.prev:
                return

        new_next = curr.next.next
        new_next.prev = curr
        curr.next = new_next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)