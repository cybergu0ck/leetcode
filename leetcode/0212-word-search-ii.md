# 212. Word Search II

Hard [level question on leetcode](https://leetcode.com/problems/word-search-ii/description/).

<br>
<br>
<br>

## Clarifications

- Minimum dimensions of the board?
  - `1 <= m, n <= 12`

- What are the characters in the board like?
  - board[i][j] is a lowercase English letter.

- Should the result contain unique words?
  - Yes

<br>
<br>
<br>

## Test cases

| Case              | Input                                                                              | Output         |
| ----------------- | ---------------------------------------------------------------------------------- | -------------- |
| Multi cell board  | board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], | ["eat","oath"] |
|                   | words = ["oath","pea","eat","rain"]                                                |                |
| Single cell board | board = ["a"],                                                                     | ["a"]          |
|                   | words = ["a"]                                                                      |                |

<br>
<br>
<br>

## Solution

<br>
<br>

### Suboptimal solution

```py
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.isEnd


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #populate the trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])
        res = []

        def dfs(i,j, word):
            if i<0 or j<0 or i>=m or j>=n or not trie.startsWith(word):
                return

            temp = board[i][j]
            word += temp
            board[i][j] = '#'

            if trie.search(word):
                res.append(word)

            dirs = [[1,0], [0,1], [-1,0], [0,-1]]
            for dr, dc in dirs:
                dfs(i+dr, j+dc, word)

            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                dfs(i,j, "")

        return list(set(res))
```

```cpp

```

<br>

#### Explanation

Build a Trie from the word list, then run a Trie-guided backtracking DFS from each board cell to find matching words.

- Construct the Trie.
- For every cell in the board
  - Run the DFS
    - Return from the DFS if the indices are out of bound or the current word formed doesn't exist in the Trie.
    - If the current word formed is present in the Trie, add it to result.
    - Cache the current character and change the value to an identifier to mark it as visited.

<br>

#### Complexity analysis

- Time Complexity : This is a Multi, $O(w*l + m*n*l*4^l)$ solution in terms of time, where $w$ is number of words, $l$ is the average length of the word, $m$ is the number of rows in the board, $n$ is the number of columns in the board.
  - The creation of the Trie is $O(w*l)$, for each word the trie's insert method is called which is $O(n)$.
  - The nested for loop is $O(m*n)$.
  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. The maximum number of nodes in a tree with depth of $n$ and each node having $k$ branches is
    $$\frac{k^{(n+1)} - 1}{k - 1}$$
  - The DFS function is $O(l*4^l)$. We can see that the number of branches is 4 (The four directions) and the depth is the average length of the word. Each recursive call calls trie's `search` method that is $O(l)$, this is the multiplation factor in the overall complexity of the DFS algo.
  - Technically, it could be stated taht DFS funciton is $O(l*3^l)$, as the algorithm never runs for all 4 directions but only 3 directions (Constrain that a character should not be used again)

- Space Complexity : This is a bi-linear, $O(w*l)$ solution in terms of space, where $w$ is the number of words added and $l$ is the average length of the words.
  - This is the worst case where all words have completely unique characters and no common prefixes, every character of every word will require a new `TrieNode`.
  - Reallistically, The strength of a Trie is prefix sharing. "apple", "apply", and "applied", all share the same first four nodes (a -> p -> p -> l). This significantly reduces the space needed compared to a hash set if many words share common beginnings.

<br>
<br>

### Efficient solution

```py

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.isEnd


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #populate the trie
        trie = Trie()

        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])
        res = []

        def dfs(i,j, node, word):
            if i<0 or j<0 or i>=m or j>=n or board[i][j] not in node.children:
                return

            ch = board[i][j]
            word += ch
            board[i][j] = '#'

            if node.children[ch].isEnd:
                res.append(word)

            dirs = [[1,0], [0,1], [-1,0], [0,-1]]
            for dr, dc in dirs:
                dfs(i+dr, j+dc, node.children[ch], word)

            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i,j, trie.root, "")

        return list(set(res))
```

```cpp

```

<br>

#### Explanation

Build a Trie from the word list, then run a Trie-guided backtracking DFS from each board cell to find matching words.

- Construct the Trie.
- For every cell in the board
  - Run the DFS
    - Return from the DFS if the indices are out of bound or the current word formed doesn't exist in the Trie.
    - If the current word formed is present in the Trie, add it to result.
    - Cache the current character and change the value to an identifier to mark it as visited.
- The approach is same as [suboptimal solution](#suboptimal-solution) but with better implementation.

<br>

#### Complexity analysis

- Time Complexity : This is a Multi, $O(w*l + m*n*4^l)$ solution in terms of time, where $w$ is number of words, $l$ is the average length of the word, $m$ is the number of rows in the board, $n$ is the number of columns in the board.
  - The creation of the Trie is $O(w*l)$, for each word the trie's insert method is called which is $O(n)$.
  - The nested for loop is $O(m*n)$.
  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. The maximum number of nodes in a tree with depth of $n$ and each node having $k$ branches is
    $$\frac{k^{(n+1)} - 1}{k - 1}$$
  - The DFS function is $O(4^l)$. We can see that the number of branches is 4 (The four directions) and the depth is the average length of the word.
  - Technically, it could be stated taht DFS funciton is $O(3^l)$, as the algorithm never runs for all 4 directions but only 3 directions (Constrain that a character should not be used again)

- Space Complexity : This is a bi-linear, $O(w*l)$ solution in terms of space, where $w$ is the number of words added and $l$ is the average length of the words.
  - This is the worst case where all words have completely unique characters and no common prefixes, every character of every word will require a new `TrieNode`.
  - Reallistically, The strength of a Trie is prefix sharing. "apple", "apply", and "applied", all share the same first four nodes (a -> p -> p -> l). This significantly reduces the space needed compared to a hash set if many words share common beginnings.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- This question is an example of how time complexity can vary for the same approach because of the implementation.
  - [suboptimal solution](#suboptimal-solution) utilises the trie and it's `search` method inside the DFS algorithm.
  - [efficient solution](#efficient-solution) avoids the `search` method call by using the Trie Node argument.

- Understanding of [Tries](./0208-implement-trie-preffix-tree.md)
  - Datastructure, implementation, uses, time and space complexities.

<br>
<br>
<br>

## Resources

\*TODO - Link the notes for Tries here

<br>
<br>
<br>
