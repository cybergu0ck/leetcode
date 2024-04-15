# Permutations

Leetcode medium level question.

<br>
<br>

## Description

Find it [here](http://rb.gy/l4sr2z)

<br>
<br>

## Solution

Use Recursive Backtracking Algorithm.

```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def foo(filled, remaining):
            if(len(filled)==len(nums)):
                ans.append(filled)
                return
            for i in range(len(remaining)):
                new_filled = filled + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                foo(new_filled, new_remaining)

        foo([], nums)
        return ans

obj = Solution()
print(obj.permute([1,2,3]))

#[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

<br>
<br>

## Learning

- Getting a list without a given index.

  ```py
  arr = arr[:i] + arr[i+1:]
  ```

<br>
<br>

## Resources

<br>
<br>
