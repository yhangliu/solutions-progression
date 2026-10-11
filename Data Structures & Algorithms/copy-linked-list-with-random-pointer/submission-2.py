"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = head
        old_map = {}
        while dummy:
            new_copy = Node(dummy.val)
            old_map[dummy] = new_copy
            dummy = dummy.next
        dummy = head
        while dummy:
            new_copy = old_map[dummy]
            if dummy.next:
                new_copy.next = old_map[dummy.next]
            if dummy.random:
                new_copy.random = old_map[dummy.random]
            dummy = dummy.next

        return old_map[head]

