# 141. Linked List Cycle

Easy [level question on leetcode](https://leetcode.com/problems/linked-list-cycle/description/).

<br>
<br>
<br>

## Clarifications

- Is it guaranteed that there is a head always? If not what should be the result for the case of no nodes in the linked list.
  - The result should be false

<br>
<br>
<br>

## Test cases

- pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

| Case                                      | Input                       | Output |
| ----------------------------------------- | --------------------------- | ------ |
| Linked list containing cycle              | head = [3,2,0,-4], pos = 1  | true   |
| Linked list doesn't containing cycle      | head = [3,2,0,-4], pos = -1 | false  |
| Linked list has only one node             | head = [3], pos = -1        | false  |
| Linked list has only one node and a cycle | head = [3], pos = 0         | true   |
| Linked list has no node                   | head = [], pos = 0          | false  |

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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while(head):
            if(head in visited_nodes):
                return True
            else:
                visited_nodes.add(head)
            head = head.next
        return False
```

```cpp

```

<br>

#### Explanation

The algorithm traverses the linked list while storing each visited node in a set, and returns True if a node is encountered more than once, indicating the presence of a cycle.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the linked list.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of nodes in the linked list .

<br>
<br>

### Efficient solution

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

```cpp

```

<br>

#### Explanation

Utilise Floyd’s Tortoise and Hare algorithm.

- Use two pointers moving at different speeds to detect a cycle in a linked list by checking if the fast and slow pointers ever meet.

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
