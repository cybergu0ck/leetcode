# Remove Nth Node From End of List

Easy level problem on leetcode.

<br>
<br>

## Description

Find it [here](http://rb.gy/9gkdop).

<br>
<br>

## Solution

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        i = 1
        while i != n:
            fast = fast.next
            i += 1
        fast = fast.next

        if not fast:
            #first node to be removed
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
```
