# 124. Binary Tree Maximum Path Sum

Hard [level question on leetcode](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/).

<br>
<br>
<br>

## Clarifications

- Is the given root always a valid node?
  - Yes

* What is the type of the node's values?
  - `-1000 <= Node.val <= 1000`

* Can the given tree contain node's with same values?
  - Yes

<br>
<br>
<br>

## Test cases

| Type             | Case                          | Input                          | Output |
| ---------------- | ----------------------------- | ------------------------------ | ------ |
| Structural       | Basic tree                    | 3, 2, 4, null, null, 10, 1     | 19     |
| Structural       | Skewed tree                   | 1, null, 2, null, 3            | 3      |
| Value constraint | Single positive root node     | 10                             | 10     |
| Value constraint | Single negtive root node      | -10                            | -10    |
| Value constraint | Include only root node        | 1, -10, -10                    | 1      |
| Value constraint | Include root + larger subtree | 10, 10, -10                    | 20     |
| Value constraint | Include only subtree          | -10, -10, 1                    | 1      |
| Value constraint | All negative nodes            | -10, -1, -30                   | -1     |
| Value constraint | Larger node present later     | 2, 1, 3, null, null, -4, 5, 10 | 14     |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py

```

```cpp

```

<br>

#### Explanation

<!-- one line desctiption of the logic of the algorithm -->
<!-- detailed explanation with steps if appropriate -->

<br>

#### Complexity analysis

- Time Complexity : This is a <!-- time complexity in english -->, $O()$ solution in terms of time, where $ $ is <!-- placeholder -->.
- Space Complexity : This is a <!-- time complexity in english -->, $O()$ solution in terms of space, where $ $ is <!-- placeholder -->.

<br>
<br>

### Efficient solution

```py
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def get_max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))

            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return max_sum
```

```cpp

```

<br>

#### Explanation

Perform recursive DFS. At each step, cache the maximum current path sum and return the maximum sum value containing node value and only one subtree.

- Recursively call the algorithm on both left and right node's of the current node, starting with root node.
- If the value returned for subtree's are negative, drop them and consider zero instead.
- Cache the maximum sum value by comparing it with current path sum (node value + left subtree value + right subtree value).
- Return only node value plus larger subtree value.
  - If both subtree's result in negative values, This approach will consider only node value.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the given tree.
  - The algorithm visits every node in the binary tree exactly once via a Depth-First Search (DFS) traversal.
  - At each node, the work done (calculating the maximum path sum and updating the nonlocal max_sum variable) involves a constant number of basic arithmetic and comparison operations ($O(1)$ work).
- Space Complexity : This is a linear, $O(h)$ solution in terms of space, This is stack space.
  - The space complexity is determined by the maximum memory allocated for the execution call stack during the recursion.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The following was my original implementation. Here a 4-way max statment is required as the maximumSum is initialised to root node's value and subtree result's are considered even if they are negative. The smart way is the consider zero instead of negative subtree results and then just consider current path (node + left + right) for maxSum check. This also requires the maxSum to be initialsed to negative infinity. This is exactly [former](#efficient-solution) approach.

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def maxPathSum(self, root: Optional[TreeNode]) -> int:
          maxSum = root.val
          def rec(root):
              if not root:
                  return 0
              onLeft = rec(root.left)
              onRight = rec(root.right)
              nonlocal maxSum
              maxSum = max(maxSum, max(onLeft + root.val, onRight + root.val, root.val + onLeft + onRight, root.val))
              return max(root.val, root.val + onLeft, root.val + onRight)
          rec(root)
          return maxSum
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
