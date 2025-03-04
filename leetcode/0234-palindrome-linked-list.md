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

- $O(n)$ solution. Brute force as it gets.

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

<br>

## Better

- $O(n/2)$ solution which is still $O(n)$. But there is a good takeway from this logic.
- Get the [middle node](0876-middle-of-the-linked-list.md) and keep a [reverse](0206-reverse-linked-list.md) list. Then initialise seg1 and seg3 correctly and then iterate over it.

    ```py
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def isPalindrome(self, head: Optional[ListNode]) -> bool:
            slow = fast = head
            rev_tail = None
            while fast and fast.next:
                fast = fast.next.next
                temp = slow.next
                slow.next = rev_tail
                rev_tail = slow
                slow = temp
            
            seg2 = slow if fast is None else slow.next  #Here
            seg1 = rev_tail

            while seg1 and seg2:
                if seg1.val != seg2.val: 
                    return False
                seg1 = seg1.next
                seg2 = seg2.next

            return True
    ```
    - If fast is None, then it means the list has Even number of nodes and the seg2 must start at slow. If fast is not None, then the list has odd number of nodes and the seg2 must start at slow.next.

<br>
<br>

## Resources

- Checkout [Middle of the Lined List](0876-middle-of-the-linked-list.md)
- Checkout [Reverse Lined List](0206-reverse-linked-list.md)

