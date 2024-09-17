# Middle of the Linked List

Easy level problem on leetcode.

<br>
<br>

## Description

Find it [here](http://rb.gy/nrugfa)

<br>
<br>

## Solution

### Brute Force

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        keys = dict()
        cur = head
        index = 0
        while cur:
            keys[index] = cur
            index += 1
            cur = cur.next

        num_nodes = len(keys)
        if(num_nodes%2 == 0):
            return keys[num_nodes/2]
        else:
            return keys[num_nodes//2]

```

<br>

### Efficient

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

<br>
<br>

## Learning

The middle of the linked list can be easily found using a slow and fast pointer.

<br>
<br>

## Resources

<br>
