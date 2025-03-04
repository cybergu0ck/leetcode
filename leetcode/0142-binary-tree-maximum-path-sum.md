# Binary Tree Maximum Path Sum

Hard level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>

### Efficient Solution

- The following has $O(n)$ time complexity $O(log(n))$ space complexity.

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def maxPathSum(self, root: Optional[TreeNode]) -> int:
          res = root.val
          def maxBranchValue(root):
              if not root:
                  return 0
              left_branch = max(maxBranchValue(root.left),0) #if the result of recursion is negative we will ignore
              right_branch = max(maxBranchValue(root.right),0)
              nonlocal res
              res = max(res, root.val + left_branch + right_branch)
              return root.val + max(left_branch, right_branch)

          maxBranchValue(root)
          return res
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- Checkout the recorded video.
- This is done following neetcodeio.

<br>
<br>

## Test Cases

<br>
<br>

## Resources

<br>
<br>
