# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict 

class Solution:
    def inOrder(self, root):
        """Is a DFS algo, use stacks. Left subtree -> Root -> Right Subtree."""
        if root == None:
            return []
        cur = root
        res, stack = [],[]
        
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            else:
                break
        return res
                
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        Traversal = self.inOrder(root)
        
        #check for duplicate nodes, if present return False
        count = defaultdict(int)
        for i in Traversal:
            count[i] += 1
        
        for i in count.values():
            if i>1:
                return False
            
        sortedTraversal = sorted(Traversal)
        
        if Traversal == sortedTraversal:
            return True
        return False
        
        