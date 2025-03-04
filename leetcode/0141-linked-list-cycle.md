# Linked List Cycle

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/linked-list-cycle/).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>

### Efficient Solution

- The following has $O(n)$ time complexity $O(1)$ space complexity using Floyd's tortoise and hare algorithm.

  ```py
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None

  class Solution:
      def hasCycle(self, head: Optional[ListNode]) -> bool:
          slow, fast = head, head

          while fast and fast.next :
              slow = slow.next
              fast = fast.next.next
              if slow == fast:
                  return True
          return False
  ```

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

## Test Cases

1. No Root, Has Cycle, No Cycle

<br>
<br>

## Resources

<br>
<br>
