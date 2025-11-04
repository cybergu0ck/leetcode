# 230. Kth Smallest Element in a BST

Medium [level question on leetcode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/).

<br>
<br>
<br>

## Clarifications

- Is 'k' always valid?

  - Yes, 1 <= k <= n <= 104. where n is the number of nodes in the tree.

- Are the values in the binary search tree unique?
  - Yes

<br>
<br>
<br>

## Test cases

| Case | Input                          | Output |
| ---- | ------------------------------ | ------ |
| BST  | root = [3,1,4,null,2], k = 1   | 1      |
| BST  | [5,3,6,2,4,null,null,1], k = 3 | 3      |

- The test case is pretty simple, the input must be a binary search tree with minimum of one node and a valid 'k'.

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):
            res = []
            cur = root
            stack = []

            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = stack.pop()
                    res.append(cur.val)
                    cur = cur.right
            return res

        inorder_sequence = inorder(root) #O(n)

        return inorder_sequence[k-1] #O(1)
```

```cpp

```

<br>

#### Explanation

Utilize inorder tree traversal.

- Pretty straightforward, get the inorder sequence and then get the necessary value from it.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the tree.
  - The inorder traversal algorithm is a linear time algorithm as the loop runs for every single node of the tree.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of nodes in the tree.
  - The inorder sequence takes up as many space as the number of nodes in the tree.
  * The stack also holds at most $O(h)$ nodes at any time, where 'h' is the height of the tree. Anyway, this is also linear.

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        cur = root
        stack = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
```

```cpp

```

<br>

#### Explanation

Utilize inorder tree traversal without creating a sequence for inorder traversal.

- The order in which the inorder sequence will be filled will be in strictly increasing order (if all values are unique), hence use the 'k' value to directly return the necessary value without creating a sequence.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(k)$ solution in terms of time, where $k$ is given input value.
  - The loop runs until 'k' nodes are visited, in the worst case `k=n`.
- Space Complexity : This is a linear, $O(h)$ solution in terms of space, where $h$ is height of the tree.
  - The stack also holds at most $O(h)$ nodes at any time, where 'h' is the height of the tree.
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
