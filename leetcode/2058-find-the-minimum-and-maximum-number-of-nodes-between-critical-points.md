# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

Medium [level question on leetcode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/).

The core problem is pattern detection and index distance measurement on a sequential structure.

- Pattern detection pertaining to identifying local maxima and minima.

<br>
<br>
<br>

## Clarifications

1. What are the size constratins of the linked list?
   - The number of nodes in the list is in the range [2, 105].

1. What is the data type of the value in the linked list node's.
   - Integers

1. Is the linked list sorted?
   - No

1. Are the values of the nodes of the linked list unique?
   - No

1. Can the linked list be modified?
   - No constraint mentioned

<br>
<br>
<br>

## Test cases

| Case                      | Type     | Input              | Output  |
| ------------------------- | -------- | ------------------ | ------- |
| No targets                | size     | [1,2]              | [-1,-1] |
| Potentially only 1 target | size     | [1,2,3]            | [-1,-1] |
| Potentially only 2 target | size     | [1,5,3,7]          | [1,1]   |
| No targets                | value    | [5,5,5,5,5]        | [-1,-1] |
| Many targets              | position | [1,5,3,1,2,2,10,7] | [1,5]   |

- Make the question simpler by considering the critical points as targets instead of focusing on local maxima and minima.
- Test cases test size constratins, value and position constraints.

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = list()
        cur = head
        prev = None
        index = 0
        while cur:
            if prev and cur.next and ((cur.val < prev and cur.val < cur.next.val) or (cur.val > prev and cur.val > cur.next.val)):
                critical_points.append(index)

            index += 1
            prev = cur.val
            cur = cur.next

        if(len(critical_points) < 2):
            return [-1,-1]

        max_d = abs(min(critical_points) - max(critical_points))
        min_d = max_d
        for i in range(1, len(critical_points)):
            cur_d = abs(critical_points[i] - critical_points[i-1])
            if cur_d < min_d:
                min_d = cur_d

        return [min_d, max_d]
```

```cpp

```

<br>

#### Explanation

Traverse the linked lis to collect critical point indices, then find distances.

- Get the list of critical point indices.
- Calculate the maximum distances between the lowest and highest values.
- Calculate the least distance between two values in the critical points.
- Return the result.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of nodes in the linked list.
  - Identifying the critical points is $O(n)$.
  - Getting the minimum and maximum values from the list of critical points and iterating over it is $O(k)$, where $k <= n$.

- Space Complexity : This is a linear, $O(k)$ solution in terms of space, where $k$ is number of critial points in the linked list.
  - This is the size for storing critical points.

<br>
<br>

### Efficient solution

```py
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_idx = -1
        prev_idx = -1
        min_d = float('inf')
        prev_val = head.val
        cur = head.next
        index = 1

        while cur.next:
            if (cur.val > prev_val and cur.val > cur.next.val) or (cur.val < prev_val and cur.val < cur.next.val):
                if first_idx == -1:
                    first_idx = index
                else:
                    min_d = min(min_d, index - prev_idx)
                prev_idx = index

            prev_val = cur.val
            cur = cur.next
            index += 1

        # If less than 2 critical points were found
        if min_d == float('inf'):
            return [-1, -1]

        max_d = prev_idx - first_idx
        return [min_d, max_d]
```

```cpp

```

<br>

#### Explanation

Perform a single pass, tracking the first and previous critical point indices to compute minimum adjacent distances on the fly and the maximum distance at the end.

- Create and update variables to track the following:
  1.  The index of the first critical point.
  1.  The index of the previous critical point.
  1.  The value of the previos node.
  1.  The minimum distance between two critical points.

- The core logic is same as [above](#brute-force), few improvements are
  - Initialise the variables and set up the loop to skip the end nodes. `head = cur.next`, `index = 1` and `while(cur.next)`.
  - Max distance can be calculated once, at the end.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of nodes in the linked list.
  - Identifying the critical points is $O(n)$.

- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Always think about acheiving without extra data strucutre, especially when storing targets to compute something like max or min later.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
