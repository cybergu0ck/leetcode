# Same Tree

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://rebrand.ly/zzen77f).

<br>
<br>

## Solution

<br>

### Brute Force

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>

### Efficient Solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case
        if (p and not q) or (q and not p):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val if (p and q) else True
```

- Solving the question using classic recursion,

  1. The base case : If one of the node exists while the other doesn't then the tree's can't be identical.
  2. The return statement: We are handling the other cases here itself, Given both nodes exist return True if the values are identical else return False. Also calling the function on both it's children.

- The following has $O(n)$ time complexity $O(log(n))$ space complexity.
  - The time complexity of the above algorithm depends on the number of recursive calls. The worst case will be when both the trees are identical, then the number of recursive calls will be equal to the number of nodes. Hence, $O(n)$.
  - The space complexity of the above algorithm depens on the depth of recursive which will be equal to the height of the binary tree. Hence, $O(log(n))$.

<br>

### Ideal Solution

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>
<br>

## Notes

<br>
<br>

## Resources

<br>
<br>
