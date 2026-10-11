class Node:
    def __init__(self, key = None, val = None):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key
        


class LRUCache:

    def __init__(self, capacity: int):
        self.nodemap = {}
        self.max_size = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.nodemap:
            return -1
        node = self.nodemap[key]
        self.delete(node)
        self.add(node)
        return node.val
        
        
    def delete(self, node):
        
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
    def add(self, new_node):
        tail = self.tail.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.tail
        self.tail.prev = new_node

    def put(self, key: int, value: int) -> None:
        #if not in map and need more space, delete then add
        if key not in self.nodemap:
            new_node = Node(key, value)
            if len(self.nodemap) >= self.max_size:
                old_node = self.head.next
                self.delete(old_node)
                del self.nodemap[old_node.key]
            self.nodemap[key] = new_node
            self.add(new_node)
        else:
            node = self.nodemap[key]
            node.val = value
            self.delete(node)
            self.add(node)
        print(self.nodemap)
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)