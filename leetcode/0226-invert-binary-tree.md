# 226. Invert Binary Tree

Easy [level question on leetcode](https://leetcode.com/problems/invert-binary-tree/description/).

<br>
<br>
<br>

## Clarifications

- Confirm the definition of inverting

  - Inverting a binary tree is the operation of swapping the left and right children of each node throughout the tree, effectively creating its mirror image.

<br>
<br>
<br>

## Test cases

| Case | Input                  | Output            |
| ---- | ---------------------- | ----------------- |
|      | root = [4,2,7,1,3,6,9] | [4,7,2,9,6,3,1]   |
|      | root = []              | []                |
|      | root = [2,3,null,1]    | [2,null,3,null,1] |

- The above test cases are complete.

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

```cpp

```

<br>

#### Explanation

Recursively swap the left and right children.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the binary tree.

  - The time complexity depends on the number of recursive calls.

- Space Complexity : This is a linear, $O(h)$ solution in terms of space, where $h$ is the depth of the binary tree.
  - In the worst case where the binary tree is skewed, the space complexity is $O(n)$ where $n$ is the number of nodes in the binary tree.
  - In the best case where the binary tree is balanced, the space complexity is $O(log(n))$ where $n$ is the number of nodes in the binary tree.

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
