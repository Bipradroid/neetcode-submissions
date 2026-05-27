# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,lower,upper):
            if not node:
                return True
            if node.val>lower and node.val<upper:
                if not node.left:
                    return dfs(node.right,max(lower,node.val),upper)
                elif not node.right:
                    return dfs(node.left,lower,min(node.val,upper))
                else:
                    return (dfs(node.left,lower,min(node.val,upper)) and 
                    dfs(node.right,max(lower,node.val),upper))
            else:
                return False
            
        return dfs(root,float("-inf"),float("inf"))

        
        