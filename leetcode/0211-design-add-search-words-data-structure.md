# 211. Design Add and Search Words Data Structure

Medium [level question on leetcode](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/).

<br>
<br>
<br>

## Clarifications

<br>
<br>
<br>

## Test cases

| Case                         | Input                                                                                | Output                                     |
| ---------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------ |
| Straight forward cases       | ["WordDictionary","addWord","addWord","addWord","search","search","search","search"] | [null,null,null,null,false,true,true,true] |
|                              | [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]                         |                                            |
| "." is present out of bounds | ["WordDictionary","addWord","search"]                                                | [null,null,false]                          |
|                              | [[],["b"],["b.."]]                                                                   |                                            |

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
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.root
        for ch in word:
            curNode = curNode.children[ch]
        curNode.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(word, root):
            curNode = root
            for i in range(len(word)):
                ch = word[i]
                if ch == ".":
                    for child in curNode.children.values():
                        if dfs(word[i+1:], child):
                            return True
                    return False

                elif ch not in curNode.children:
                    return False
                curNode = curNode.children[ch]
            return curNode.isEnd

        return dfs(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

```cpp

```

<br>

#### Explanation

Use a Trie datastrucutre and use DFS for handling "."

- `addWord` is standard Trie implementation.
- The `search` method needs to be tweaked to include the logic for handling '.'. Whenever a '.' is encountered within bounds, we consider the search to be True until then and call the same logic for the remaining part of the word with the subsequent parts of the Trie. Since a Trie node's children can have multiple child's we need to do DFS until one word matches.

<br>

#### Complexity analysis

- Time Complexity :

1. Add : This is a linear, $O(n)$ solution in terms of time, where $n$ is length of the word being added.
1. Search : This is a linear, $O(N)$ solution in terms of time, where $N$ is number of nodes in the Trie tree.
   - In a simple list using linear search, it will be $O(m*l)$ where $m$ is the number of words and $l$ is the average length of the words. However, this is not likely case in Tries because of preffix sharing however in the worst case scenario where preffix sharing is absent it will be the case. Even then it is preffered to state Big O in terms of nodes to describe tree traversal.

- Space Complexity : This is a bi-linear, $O(m*l)$ solution in terms of space, where $m$ is the number of words added and $l$ is the average length of the words.
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

<br>
<br>
<br>

## Resources

- Checkout [neetcode's]() video. It is similar to my implementaiton.

<br>
<br>
<br>
