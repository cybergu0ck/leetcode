# 21. Merge Two Sorted Lists

Easy [level question on leetcode](https://leetcode.com/problems/merge-two-sorted-lists/description/).

<br>
<br>
<br>

## Clarifications

1. Can the head pointers be null?

   - Yes

1. Can the linked lists contain duplicate values?

   - Yes, the final result should have "non-decreasing" order of values.

<br>
<br>
<br>

## Test cases

| Case                 | Input       | Output    |
| -------------------- | ----------- | --------- |
| Empty pointers       | [] []       | []        |
| One pointer is empty | [] [1,3]    | [1,3]     |
| Normal lists         | [1,4] [2,3] | [1,2,3,4] |
| Repeated elements    | [1,2] [1,2] | [1,1,2,2] |

- The above test cases looks complete.

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

A brute force version might:

1. Traverse both linked lists and copy all the values into a Python list.
2. Sort the combined list.
3. Create a new linked list from the sorted values. (Although the question asks to do everything in-place)

<br>

#### Complexity analysis

- Time Complexity : This is a log-linear, $O((n+m) log(n+m))$ solution in terms of time, where $n$ and $m$ are the number of nodes in the two linked lists.
- Space Complexity : This is a linear, $O(n+m)$ solution in terms of space, where $n$ and $m$ are the number of nodes in the two linked lists.

<br>
<br>

### Efficient solution

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        if not list1 or not list2:
            res = list1 or list2
        else:
            res = list1 if list1.val < list2.val else list2
            if res == list1:
                list1 = list1.next
            else:
                list2 = list2.next
            cur = res
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 or list2

        return res
```

```cpp

```

<br>

#### Explanation

Starting with the smaller head, iterate through both lists and repeatedly link the smaller current node to build a merged list.

- Check the validity of the head's. If both head's are invalid return None. If one is valid and another is not, return the valid head.
- If both heads are valid, Pick the head that has smaller value to start with and update that pointer to point to it's next.
- Create a variable to keep track of current node.
- Iterate until both the heads are valid, keep updating the current node and the head's.
- If one head becomes invalid and other is valid, ensure the valid one is appended at the end of the current node.
- return the starting head.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n+m)$ solution in terms of time, where $n$ and $m$ are the number of nodes in the two linked lists.
  - In the worst case, where both lists have equal number of nodes each node will be visited.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The elegant way to code up the following

  ```py
  if not a and not b:
      return None
  elif not a:
      return b
  elif not b:
      return a
  ```

  ```py
  if not a or not b:
      return a or b
  ```

- To make a function having multiple return statments to one return statement.

  ```py
  if condition1:
      return something
  else:
      return something_else
  ```

  ```py
  res = None

  if condition1:
      res = something
  else:
      res = something_else

  return res
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
