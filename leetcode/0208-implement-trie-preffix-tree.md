# 208. Implement Trie (Prefix Tree)

Medium [level question on leetcode](https://leetcode.com/problems/implement-trie-prefix-tree/description/).

<br>
<br>
<br>

## Clarifications

- Can an empty word be added?
  - No, `1 <= word.length, prefix.length <= 2000`

- Can an existing word be added again?
  - Yes

- What is the type of characters in the word?
  - `word` and `prefix` consist only of lowercase English letters.

<br>
<br>
<br>

## Test cases

|        | Order of ops                                                       |
| ------ | ------------------------------------------------------------------ |
| Input  | ["Trie","insert","search","search","startsWith","insert","search"] |
|        | [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]           |
| Output | [null, null, true, false, true, null, true]                        |

<br>
<br>
<br>

## Solution

<br>
<br>

### Bilinear brute force solution

```py

```

```cpp

```

<br>

#### Explanation

Use an array datastructure and perform string operations.

<br>

#### Complexity analysis

- Time Complexity :
  - Add : This would be a constant, $O(1)$ to add a word to the array data structure.
  - Search : This would be a bi-linear, $O(n*m)$ where $n$ is the number of words stored and $m$ is the average length of the words. The algorithm is essentially a linear scan, in the worst case every word must be checked for every character.
  - Startswith : This would be a bi-linear, $O(n*m)$ where $n$ is the number of words stored and $m$ is the average length of the words. The algorithm is essentially a linear scan, in the worst case every word must be checked for every character.

- Space Complexity : This is a bi-linear, $O(n*m)$ solution in terms of space, where $n$ is the number of words stored and $m$ is the average length of the words.
  - Here, we are talking about the memory required to store all the characters!

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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

```cpp

```

<br>

#### Explanation

Classic trie implementation using defaultdict.

- Note that the same can be acheived with a normal `dict`.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m)$ solution in terms of time, where $m$ is the length of the word.
  - Add : This is a linear, $O(m)$ solution in terms of time, where $m$ is the length of the word.
  - Search : This is a linear, $O(m)$ solution in terms of time, where $m$ is the length of the word.
  - Startswith :This is a linear, $O(m)$ solution in terms of time, where $m$ is the length of the word.
  - In every case the algorithm runs for each character of the word throught the Trie-based tree.

- Space Complexity : This is a bi-linear, $O(n*m)$ solution in terms of space, where $n$ is the number of words stored and $m$ is the average length of the words.
  - Here, we are talking about the memory required to store all the characters!
  - Although the space complexity is better than the above on average as there is `TrieNode` is reused. Example : "apple" and "app".

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- It is important to note that the `isEnd` attribute of a `TrieNode` is set True for the subsequent node of the last character's `TrieNode` and not on itself.
  - The final `TrieNode` represents the 'End State' reached by that character rather than the character itself.
  - If the understanding is that the `isEnd` attribute of `TrieNode` containing the last character for a word itself will be made True, then this means that the character itself is considered, this understanding is faulty as the `TrieNode` consists of other characters as well and it would mean that all those other characters can also be considered terminal, which is not the case!

    ![image](./_assets/images/leetcode-208-1.jpg)

<br>
<br>
<br>

## Resources

- Checkout [Tushar's](https://www.youtube.com/watch?v=AXjmTQ8LEoI) explanation about Trie datastructure.

<br>
<br>
<br>
