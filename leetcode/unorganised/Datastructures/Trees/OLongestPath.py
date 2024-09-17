"""

Py files in the leetcode directory which starts with O means its question out of leetcode!

Given the root of a binary tree, return the list of nodes that make up the longest path from root to leaf node.

"""

class Node:
    def __init__(self, val, left = None, right =None):
        self.val = val
        self.left = left
        self.right = right
    
    def longestPath(self,root):
        if not root:
            return []
        
        return [root.val] + self.argmax(self.longestPath(root.left), self.longestPath(root.right))

    def argmax(self, list1, list2):
        return list1 if len(list1) >= len(list2) else list2

"""
say the binary tree is 

                   1
                 /   \
               2      3
              / \    / \
             4   5  6   7
                   / \
                  8   9
                 /
                10  

We need the output as [1,3,6,8,10]

"""



Root = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)
Node8 = Node(8)
Node9 = Node(9)
Node10 = Node(10)

Root.left = Node2
Root.right = Node3
Node2.left = Node4
Node2.right = Node5
Node3.left = Node6
Node3.right = Node7
Node6.left = Node8
Node6.right = Node9
Node8.left = Node10

print(Root.longestPath(Root))