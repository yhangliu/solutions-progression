class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if self.capacity == len(self.map):
                node = self.head.next
                self.remove(node)
                del self.map[node.key]
            node = ListNode(key, value)
            self.insert(node)
            self.map[key] = node


    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        tail = self.tail
        prev = tail.prev

        prev.next = node
        node.prev = prev
        node.next = tail
        tail.prev = node
        
