# 206. Reverse Linked List

Easy [level question on leetcode](https://leetcode.com/problems/reverse-linked-list/description/).

<br>
<br>
<br>

## Clarifications

1. Can the head pointer be null?

   - Yes, the reverse of it is also null.

<br>
<br>
<br>

## Test cases

| Case       | Input   | Output  |
| ---------- | ------- | ------- |
| empty list | []      | []      |
| basic list | [1,2,3] | [3,2,1] |

- The test cases are complete for the question.

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

1. Iterate over the linked list and store the values in a python list, reverse the python list and then create a new linked list.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of nodes in the linked list.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the size of the python list used to store the node's values.

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
```

```cpp

```

<br>

#### Explanation

Iteratively, at each step, store the next node, point the current node to the previous, then advance previous to current, and current to the stored next.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of nodes in the linked list.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

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
