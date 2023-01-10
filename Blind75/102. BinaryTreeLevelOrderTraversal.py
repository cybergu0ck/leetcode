# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """BFS Algo, must use queues. Also, 2 while loops as they need [[]]"""
        if root == None:
            return None
        
        cur = root
        res, q = [], [root]
        
        while q:
            ans = []
            qSize = len(q)
            while qSize >0 :
                cur = q.pop(0)
                qSize -= 1
                ans.append(cur.val)
                
                if cur.left:
                    q.append(cur.left) 
                if cur.right:
                    q.append(cur.right)
                
            res.append(ans)
            
        return res
            