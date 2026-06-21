# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode()
        builder = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tmp = curr1.next
                builder.next = curr1
                builder = curr1
                curr1 = tmp
            else:
                tmp = curr2.next
                builder.next = curr2
                builder = curr2
                curr2 = tmp
        
        if curr1:
            builder.next = curr1
        if curr2:
            builder.next = curr2
        
        return dummy.next
        