# 102. Binary Tree Level Order Traversal

Medium [level question on leetcode](https://leetcode.com/problems/binary-tree-level-order-traversal/).

<br>
<br>
<br>

## Clarifications

- What is the expected answer if there is not root.
  - Answer must be []

<br>
<br>
<br>

## Test cases

| Case        | Input   | Output      |
| ----------- | ------- | ----------- |
| No root     | []      | []          |
| Single node | [1]     | [[1]]       |
| Many nodes  | [1,2,3] | [[1]],[2,3] |

<br>
<br>
<br>

## Solution

<br>
<br>

### Quadratic brute force solution

```py
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root] if root else []

        while q:
            level = []
            for _ in range(len(q)):
                cur = q.pop(0) #O(n)
                level.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res
```

```cpp

```

<br>

#### Explanation

Perform breadth first traversal using queue.

- Detailed explanation is as follows:
  - Start with the root node and put it in a queue.
  - While the queue is not empty, repeat the following steps:
  - Create a list to store the values of nodes at the current level.
  - For each node in the queue:
    - Remove the node from the queue.
    - Add its value to the current level list.
    - If the node has a left child, add it to the queue.
    - If the node has a right child, add it to the queue.
  - Add the current level list to the result.
  - Continue until all levels are processed and the queue is empty.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the number of nodes.

  - The quadratic space complexity is not because of the nested loops, even though there are nested loops each node is processed only once.
  - The quadratic space complexity is because of the list data structure's `pop(0)` method, all the nodes need to rearranged hence this itself is an $O(n)$ operation.
  - Each node is visited once ($O(n)$) and in every visit the nodes in the corresponding level needs to be re-arrannged ($O(n)$), Overall $O(n^2)$.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is number of nodes.
  - The `res` variable stores all the nodes.
  - The maximum length of the queue variable would be the level that contains the most number of nodes.

<br>
<br>

### Linear solution

```py
from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root]) if root else []

        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res
```

```cpp

```

<br>

#### Explanation

Perform breadth first traversal using queue and use collection.deque specifically.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes.
  - Each node is visited only once and the `deque.popleft` method is $O(1)$ time.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of nodes.

<br>
<br>

### Elegant linear solution

```py
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root] if root else []

        while q:
            res.append([node.val for node in q])
            q = [child for node in q for child in (node.left, node.right) if child]
        return res
```

```cpp

```

<br>

#### Explanation

Perform breadth first traversal using a list and list comprehension without popping anything.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes.

  - Each node is visited only once and every node is thus visited.
  - There is no popping operation, the queue variable is just replaced with the new list.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of nodes.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Consider the time complexity explicitely when popping operation is performed.

  - Python list's `pop(0)` operation is a linear time operation $O(n)$.
  - Collection.deque's `popleft()` operation is a constant time operation $O(1)$.

- Understand Python's list comprehension with if condition and also nested list comphrension and with both. See [noes](https://github.com/cybergu0ck/notes/blob/main/engineering/software/programming/python/02-data-types/lists.md).

- Nesting while loops will need an additional variable. Hence better to use a while and a nested for loop.

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
          res = []
          if root:
              q = [root]
              while q:
                  level = []
                  original_size = len(q)
                  while original_size>0:
                      cur = q.pop(0) #Remeber to pop the first value, It is a Queue!
                      level.append(cur.val)
                      original_size -=1
                      if cur.left:
                          q.append(cur.left)
                      if cur.right:
                          q.append(cur.right)
                  res.append(level)
          return res
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
