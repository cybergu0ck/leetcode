# 98. Validate Binary Search Tree

Medium [level question on leetcode](https://leetcode.com/problems/validate-binary-search-tree/description/).

<br>
<br>
<br>

## Clarifications

- Is an empty tree a valid BST?
  - The inputs always contain a minimum of 1 node.

<br>
<br>
<br>

## Test cases

| Case        | Input                 | Output |
| ----------- | --------------------- | ------ |
| Valid BST   | root = [2,1,3]        | True   |
| Invalid BST | [5,1,4,null,null,3,6] | False  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        max_until_now = float('-inf')
        stack = []
        cur = self.root if not root else root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if max_until_now == float('-inf'):
                    max_until_now = cur.val
                else:
                    if cur.val <= max_until_now:
                        return False
                    else:
                        max_until_now = cur.val
                cur = cur.right

        return True
```

```cpp

```

<br>

#### Explanation

Utilize inorder traversal and check the consistency of values.

- Tweak the inorder traversal algorithm to check if the node's values are consistent with the binary search tree property.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the binary tree.
  - The algorithm iterates once for every node in the tree.
- Space Complexity : This is a lienar, $O(h)$ solution in terms of space, where $h$ is height of the binary tree.
  - For a balanced BST, h = $O(\log n)$
  - For a skewed tree, h = $O(n)$

<br>
<br>

### Linear elegant solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, left, right):
            if not node:
                return True
            elif not left < node.val < right:
                return False
            return check(node.left, left, node.val) and check(node.right, node.val, right)

        return check(root, float('-inf'), float('inf'))
```

```cpp

```

<br>

#### Explanation

Recursively check if current node value is less than the minimum value and greater than the maximum value.

- Utilize a recursive function that accepts a node, minimum value, maximum value.
- For the root, the minimum and maximum values are `float('-inf)` and `float('inf')`respectively.
- For the left subtree's the minimum and maximum values are `float('-inf)` and the value of the current node respectively.
- For the right subtree's the minimum and maximum values are the value of the current node and `float('inf)` respectively.
- Note the base case's.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the binary tree.
  - The algorithm iterates once for every node in the tree.
- Space Complexity : This is a lienar, $O(h)$ solution in terms of space, where $h$ is height of the binary tree.
  - For a balanced BST, h = $O(\log n)$
  - For a skewed tree, h = $O(n)$

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
