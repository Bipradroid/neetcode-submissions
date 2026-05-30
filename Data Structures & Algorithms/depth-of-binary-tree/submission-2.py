# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            level=[]
            q_len=len(q)
            for _ in range(q_len):
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
                    
            if level:
                res.append(level)
        return len(res)