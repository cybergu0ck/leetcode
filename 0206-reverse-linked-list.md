# Reverse Linked List

Leetcode easy level question.

<br>
<br>

## Description

Find it [here](http://rb.gy/1nj72g)

<br>
<br>

## Solution

<br>

- $O(n)$ solution.

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

<br>
<br>

## Resources

<br>
<br>
