# 133. Clone Graph

Medium [level question on leetcode](https://leetcode.com/problems/clone-graph/description/).

<br>
<br>
<br>

## Clarifications

- Can there be self loops?
  - No

<br>
<br>
<br>

## Test cases

| Case | Input | Output |
| ---- | ----- | ------ |
|      |       |        |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def dfs(node, visited):
            if node in visited:
                return visited[node]

            newNode = Node(node.val)
            visited[node] = newNode
            neighbors = []
            for neighbor in node.neighbors:
                neighbors.append(dfs(neighbor, visited))
            newNode.neighbors = neighbors
            return newNode

        visited = dict()
        return dfs(node, visited)
```

```cpp

```

<br>

#### Explanation

Run DFS recursively while creating new node, iterate over the neighbors and call DFS on it and update the neighbor class attribute at the end of DFS.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(V+E)$ solution in terms of time, where $V$ is the number of vertices (nodes) and $E$ is the number of edges.
  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree.
  - The if `node in visited` check ensures that each unique node in the original graph is processed exactly once. This takes $O(V)$.
  - For every node visited, you iterate through its neighbors list. Across the entire execution, you will look at every edge in the graph exactly twice (once from each end of the edge in an undirected graph). This takes $O(E)$.

- Space Complexity : This is a linear, $O(V)$ solution in terms of space, where $V$ is the number of vertices (nodes).
  - This dictionary stores a mapping for every node in the graph. It contains $V$ entries, resulting in $O(V)$ space.
  - In the worst-case scenario (e.g., a graph that is essentially one long line/path), the depth of the recursive calls can reach $V$. This takes $O(V)$ space.
  - The new graph creation requires $V$ new Node objects.

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
