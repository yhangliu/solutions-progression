# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = []
        num_2 = []

        while l1:
            num_1.append(l1.val)
            l1 = l1.next
        while l2:
            num_2.append(l2.val)
            l2 = l2.next

        num_1 = num_1[::-1] 
        num_2 = num_2[::-1]


        num_1_len = len(num_1)
        num_2_len = len(num_2)
        sum_1 = 0
        sum_2 = 0
        for i in range(num_1_len):
            sum_1 += int(num_1[i]) * pow(10, num_1_len - i - 1)
        for i in range(num_2_len):
            sum_2 += int(num_2[i]) * pow(10, num_2_len - i - 1)
        output_num = str(sum_1 + sum_2)[::-1]

        dummy = ListNode()
        head = dummy
        for num in output_num:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return head.next

        