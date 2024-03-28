# Palindrome Linked List

Easy level problem on leetcode.

<br>
<br>

## Description

Find it [here](http://rb.gy/14xn4w).

<br>
<br>

## Solution

<br>

### Brute Force

- $O(n)$ solution.

  ```py
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  import math
  class Solution:
      def isPalindrome(self, head: Optional[ListNode]) -> bool:
          arr = []
          cur = head
          while cur:
              arr.append(cur.val)
              cur = cur.next

          size_arr = len(arr)
          mid_index = size_arr//2

          if(len(arr)<2):
              return True

          else:
              if(size_arr%2 == 0):
                  first_half = arr[:mid_index]
                  second_half = arr[mid_index:]

              else:
                  first_half = arr[:mid_index]
                  second_half = arr[mid_index+1:]

              if first_half == second_half[-1::-1]:
                  return True

              else:
                  return False
  ```
