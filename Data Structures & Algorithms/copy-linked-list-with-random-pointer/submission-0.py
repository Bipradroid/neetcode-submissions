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
        
        new_head = Node(head.val, None, None)
        new = new_head

        current = head
        node_dict = {current: 0}
        new_node_dict = {0: new_head} 
        c = 1
        while current.next: 
            current = current.next
            node_dict[current] = c
            new_head.next = Node(current.val, None, None)
            new_node_dict[c] = new_head.next
            new_head = new_head.next
            c += 1

        current = head
        new_head = new
        while current:
            if not current.random:
                new_head.random = None
            else:
                rnd_idx = node_dict[current.random]
                rdn_node = new_node_dict[rnd_idx]
                new_head.random = rdn_node

            current = current.next
            new_head = new_head.next
        
        return new
        