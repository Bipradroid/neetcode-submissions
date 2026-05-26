# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            qLen=len(q)
            bfs=[]
            for _ in range(qLen):
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    bfs.append(node.val)
            if bfs:
                res.append(bfs[-1])
        return res

        