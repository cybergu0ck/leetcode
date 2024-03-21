# Insertion Sort List

Leetcode medium level question.

<br>
<br>

## Description

Find it [here](http://rb.gy/n391x5)

<br>
<br>

## Solution

- $O(n^2)$ solution

  ```py
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          copy = ListNode(0, head)
          prev = head
          cur = head.next

          while cur:
              if prev.val <= cur.val:
                  prev = prev.next
                  cur = cur.next
                  continue
              temp = copy
              while temp.next.val < cur.val:
                  temp = temp.next
              prev.next = cur.next
              cur.next = temp.next
              temp.next = cur
              cur = prev.next

          return copy.next
  ```
