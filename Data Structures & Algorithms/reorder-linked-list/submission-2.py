# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast .next.next
        
        prev = None
        temp = slow.next
        slow.next = None
        slow = temp

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while head and prev:
            temp_head = head.next
            temp_prev = prev.next
            head.next = prev
            prev.next = temp_head
            prev = temp_prev
            head = temp_head
            

        
        