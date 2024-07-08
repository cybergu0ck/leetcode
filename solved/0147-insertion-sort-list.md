# Insertion Sort List

Leetcode medium level question.

<br>
<br>

## Description

Find it [here](http://rb.gy/n391x5)

<br>
<br>

## Solution

- $O(n^2)$ solution.
- The logic is very similar to insertion sort algorithm, only difference is that unlike arrays singly linked list's donot have pointer to previous, hence we create a dummy start node and then iterate in forward direction (traditionally we iterate backward in the insertion sort algorithm).

  ```py
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          start = ListNode(0, head)
          prev = head
          cur = head.next

          while cur:
              if prev.val <= cur.val:
                prev = prev.next
                cur = cur.next
              else:
                copy = start
                while copy.next.val < cur.val:
                    copy = copy.next
                prev.next = cur.next
                cur.next = copy.next
                copy.next = cur
                cur = prev.next

          return start.next
  ```
