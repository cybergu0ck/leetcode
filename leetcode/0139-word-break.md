# 139. Word Break

Medium [level question on leetcode](https://leetcode.com/problems/word-break/description/).

<br>
<br>
<br>

## Clarifications

1. Is the string comprised of unique characters?
   - No

1. Can the string be empty?
   - `1 <= s.length <= 300`

1. Can the wordDict array be empty?
   - `1 <= wordDict.length <= 1000`

1. Are the words in wordDict unique?
   - Yes

<br>
<br>
<br>

## Test cases

| Case               | Input                                                         | Output |
| ------------------ | ------------------------------------------------------------- | ------ |
| True case          | s = "leetcode", wordDict = ["leet","code"]                    | True   |
| False case         | s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] | False  |
| Index matters case | s = "ccbb", wordDict = ["bc","cb"]                            | False  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Top down recursive solution

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True
            for word in wordDict:
                curWord = s[i::]
                if curWord.startswith(word):
                    if dfs(i+len(word)):
                        return True
            return False

        return dfs(0)
```

```cpp

```

<br>

#### Explanation

Since the question has both "Optimal substructure" and "Overlapping subproblems", we can try Dynamic programming's framework.

- The question has "Optimal substructure".
  - Suppose we have to check if "leetcode" is breakable and we have "leet" in the wordDict. The whole word can be breakable if the rest of the word (i.e. "code") is breakable.

- The questin has "Overlapping subproblems".
  - Suppose s = "catsanddog" and wordDict = ["cat", "cats", "and", "sand", "dog"].
  - For word break at "cat" + "sanddog", we will eventually end up with "dog" down the line.
  - For word break at "cats" + "anddog", we will eventually end up with "dog" down the line too.

<br>

1.  Define the objective function.

    $T(i)$ is whether the substring `s[i:]` can be segmented into words from `wordDict`.

2.  Identify the base cases.

    $T(len(s)) = True$
    - Empty suffix is breakable.

3.  Form the recurrance relation.

    $T(i) = T(i + len(word)) \quad \text{if word is present in wordDict and s[i:] startswith word}$
    - This is a recursive leap of faith and suffix based approach, If the word at current index is segmented until index say $j$ then we assume our recursive solution will find the solution for the remaining part of the strings. That is we assume to know the solution of the future subproblems.

4.  Find the answer.

    Result is True if index reaches the length of the given word, meaning the whole word is breakable otherwise it is false.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(k^n)$ solution in terms of time, where $k$ is the number of words in the `wordDict` and $n$ is the length of the input string `s`.
  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. The maximum number of nodes in a tree with depth of $n$ and each node having $k$ branches is

  $$\frac{k^{(n+1)} - 1}{k - 1}$$
  - It might not be intuitive to determine the worst case scenario for this question at first, the worst case scenario occurs for instances where `s='aaaa'` and `wordDict = ['a']`.
  - The depth of the recursion tree is equal to the length of the input string $n$. The number of branches at each node is equal to the number of words in `wordDict`, $k$.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is length of the input string.
  - This is the space consumed by recursion stack.

<br>
<br>

### Top down recursive solution with memoization

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = dict()
        def dfs(i):
            if i in mem:
                return mem[i]
            if i == len(s):
                return True
            for word in wordDict:
                curWord = s[i::]
                if curWord.startswith(word):
                    if dfs(i+len(word)):
                        mem[i] = True
                        return True
            mem[i] = False
            return False

        return dfs(0)
```

```cpp

```

<br>

#### Explanation

Memoize the [above](#top-down-recursive-solution) solution using a map.

<br>

#### Complexity analysis

- Time Complexity : This is a bilinear, $O(n*k)$ solution in terms of time, where $n$ is length of the input string and $k$ is the number of words in the `wordDict` array.
  - By cacheing the calculated values, we avoid repeated calculations.
  - The recursive function runs once for each index in the input string.
  - The recursive function itself is a $O(k)$, where $k$ is the length of the `wordDict` array. This is the looping.
  - Hence overall it is $O(n*k)$.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is length of the input string.
  - Space used by the map.
  - Space is used by the recursive stack as well.

<br>
<br>

### Bottom up solution

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False for i in range(length+1)]
        dp[length] = True
        for i in range(length-1,-1,-1):
            for word in wordDict:
                curWord = s[i::]
                if curWord.startswith(word) and dp[i+len(word)]:
                    dp[i] = True

        return dp[0]
```

```cpp

```

<br>

#### Explanation

Use 1D array and recurrance relation to code the bottom up dp approach.

- Note that the direction is in reverse from right to left because the recurrance relation is setup in such a way that we know the solutions to future subproblems.

<br>

#### Complexity analysis

- Time Complexity : This is a bilinear, $O(n*k)$ solution in terms of time, where $n$ is length of the input string and $k$ is the number of words in the `wordDict` array.
  - The outer loop is of $O(n)$ time.
  - The inner loop is of $O(k)$ time.
  - Overall the time is of $O(n*k)$.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is target value.
  - Space used by the 1D array.
  - There is no recursion stack here.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- It is important to know how the recurance relation is setup, if it setup in such a way that we must know the solution to future subproblems then while implmenting the bottom up approch it is most likely iterates in reverse direction for index based data structures.
- The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. The maximum number of nodes in a tree with depth of $n$ and each node having $k$ branches is

  $$\frac{k^{(n+1)} - 1}{k - 1}$$

- Note that the index plays a crucial role here, The following implementation is misleading as it passes basic test cases. Here the index is not at all considered and fails for a test case like `s = "ccbb", wordDict = ["bc","cb"]`.

  ```py
  class Solution:
      def wordBreak(self, s: str, wordDict: List[str]) -> bool:
          def dfs(word):
              if word == "":
                  return True
              for item in wordDict:
                  if item in word:
                      removedWord = word.replace(item, "")
                      if dfs(removedWord):
                          return True
              return False

          return dfs(s)
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
