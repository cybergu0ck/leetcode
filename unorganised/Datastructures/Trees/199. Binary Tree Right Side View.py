# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def foo(listRight,listLeft):
            """Basically gives priority to the nodes on the Right Side view, appends longer left side nodes."""
            if len(listLeft) > len(listRight):
                for i in range(len(listRight)):
                    listLeft.pop(0)

                return listRight + listLeft
            else:
                return listRight
            
        if not root:
            return []
        
        return [root.val] + foo(self.rightSideView(root.right),self.rightSideView(root.left))
    
    
    
        