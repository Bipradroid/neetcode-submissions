# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenght = 0
        current = head
        while current is not None:
            lenght += 1
            current = current.next
        
        target = lenght - n - 1

        if target == -1:
            head = head.next
        
        c = 0
        current = head
        while current is not None:
            if c == target:
                current.next = current.next.next
            c += 1
            current = current.next
        
        return head
        