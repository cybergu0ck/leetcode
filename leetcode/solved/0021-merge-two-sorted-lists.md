# Merge Two Sorted Lists

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://rebrand.ly/4t4p9zb).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>

### Efficient Force

- The following has $O(n)$ time complexity $O(1)$ space complexity.

  ```py
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          root = ListNode()
          cur = root
          while list1 and list2:
              if list1.val <= list2.val:
                  cur.next = list1
                  list1 = list1.next
              else:
                  cur.next = list2
                  list2 = list2.next
              cur = cur.next
          if list1:
              cur.next = list1
          if list2:
              cur.next = list2
          return root.next
  ```
- Time complexity is actually $O(n+m)$.
- For the curious, we don't need to check both list1 and list2 at the end, we can instead use an if else.
  
<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>
<br>

## Notes



<br>
<br>

## Resources

<br>
<br>
