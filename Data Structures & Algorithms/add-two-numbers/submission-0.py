# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        s1 = ""
        s2 = ""
        while curr1:
            s1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            s2 += str(curr2.val)
            curr2 = curr2.next
        s1 = s1[::-1]
        s2 = s2[::-1]
        str_s = str(int(s1) + int(s2))
        str_s = str_s[::-1]
        dummy = ListNode(0)
        tail = dummy

        for ch in str_s:
            tail.next = ListNode(int(ch))
            tail = tail.next

        return dummy.next

        