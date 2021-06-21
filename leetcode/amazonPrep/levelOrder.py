# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = []
        
        q.append(root)
        output = []
        
        while q:
            n = len(q)
            
            level = []
            
            for i in range(n):
                node = q.pop(0)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)                
                
                level.append(node.val)
            
            output.append(level)
            
        return output
            
        
        