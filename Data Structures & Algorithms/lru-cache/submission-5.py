class ListNode: 
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.key = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self.remove(key)
            self.add(key, node.value)
            return self.key_map[key].value
        return - 1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key_map:
            if len(self.key_map) == self.capacity:
                self.remove(self.head.next.key)
            self.add(key, value)
        else:
            self.remove(key)
            self.add(key, value)
    def add(self, key, value):
        new_node = ListNode(value)
        old = self.tail.prev
        old.next = new_node
        new_node.key = key
        new_node.prev = old
        new_node.next = self.tail
        self.tail.prev = new_node
        self.key_map[key] = new_node
    def remove(self, key):
        to_remove = self.key_map[key]
        prev = to_remove.prev
        next = to_remove.next
        prev.next = next
        next.prev = prev
        del self.key_map[key]
        
