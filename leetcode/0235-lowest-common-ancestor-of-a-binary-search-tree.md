# 235. Lowest Common Ancestor of a Binary Search Tree

Medium [level question on leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/).

<br>
<br>
<br>

## Clarifications

1. Is it guaranted that there exists a common ancestor in every case.

   - It is given that $p$ and $q$ will exist in the binary search tree. Therefore, a common ancestor will exist.

1. Can p and q be same node?

   - It is given that `p != q`

1. Are node values unique?

   - It is given that node values are unique.

<br>
<br>
<br>

## Test cases

| Case                                                                     | Input                                           | Output |
| ------------------------------------------------------------------------ | ----------------------------------------------- | ------ |
| p and q are on different subtrees                                        | [6, 2, 8] and p = 2 and q = 8                   | 6      |
| p is root node and q exists in right subtree                             | [6, 2, 8] and p = 6 and q = 8                   | 6      |
| q is root node and q exists in left subtree                              | [6, 2, 8] and p = 2 and q = 6                   | 6      |
| p is root node and q exists in left subtree and there's no right subtree | [6, 2] and p = 6 and q = 2                      | 6      |
| p is root node and q exists in right subtree and there's no left subtree | [6, null, 8] and p = 6 and q = 8                | 6      |
| p and q exist in left subtree                                            | [6, 2, 8, 1, 3] and p = 1 and q = 3             | 2      |
| p and q exist in right subtree                                           | [6, 2, 8, null, null, 7, 9] and p = 7 and q = 9 | 8      |

- Consider equvivalent set of test cases by flipping p and q nodes in the above cases.
- The above test cases are complete set for the question.

<br>
<br>
<br>

## Solution

<br>
<br>

### Recusrsive solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val < root.val and q.val > root.val) or (p.val> root.val and q.val < root.val) or (p.val == root.val or q.val == root.val):
            return root

        elif (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
```

```cpp

```

<br>

#### Explanation

Use the property of binary search tree and recursion.

- Starting from the root node, compare p and q values with the root node value and subsequently call the recursive function on either left child or right child.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(h)$ solution in terms of time, where $h$ is height of the binary search tree.
  - In the worst case, `cur` will be updated as long as the height of the binary search tree.
  - Time complexity in terms of number of nodes $n$ can be logarithmic, $O(log(n))$ for balanced BST and linear, $O(n)$ for skewed BST.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space due to the recursion call stack.

<br>
<br>

### Iterative solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if(p.val <= cur.val and q.val >= cur.val) or (q.val <= cur.val and p.val >= cur.val):
                return cur
            elif p.val <= cur.val and q.val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right
```

```cpp

```

<br>

#### Explanation

Use the property of binary search tree.

- Starting from the root node as current node, compare p and q values with the current node value and update the current node until the result node is found.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(h)$ solution in terms of time, where $h$ is height of the binary search tree.
  - In the worst case, `cur` will be updated as long as the height of the binary search tree.
  - Time complexity in terms of number of nodes $n$ can be logarithmic, $O(log(n))$ for balanced BST and linear, $O(n)$ for skewed BST.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Note that the condition used in the first `if` block in both the recursive solution and the iterative solution can be interchanged as they are same!

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
