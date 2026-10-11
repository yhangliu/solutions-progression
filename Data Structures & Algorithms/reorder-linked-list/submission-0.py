# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        curr = ListNode()
        dummy = curr
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        slow = temp
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while head and prev:
            next_first = head.next
            next_second = prev.next
            curr.next = head
            curr = curr.next
            curr.next = prev
            curr = curr.next
            head = next_first
            prev = next_second
        
        curr.next = head
        

        