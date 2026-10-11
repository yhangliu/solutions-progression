# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        dummy = ListNode()
        dummy.next = head

        while head:
            head = head.next
            list_length += 1
        target = list_length - n

        current = dummy

        for i in range(target):
            current = current.next
        current.next = current.next.next

        return dummy.next
        