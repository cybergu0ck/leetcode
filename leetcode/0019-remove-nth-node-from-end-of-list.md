# Template

Medium [level question on leetcode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/).

<br>
<br>
<br>

## Clarifications

- Is "n" always valid? For example if there are 3 nodes then can n be 4?

  - No, 1 <= n <= sz; where sz is the number of nodes in the list.

- Can n = 0?

  - No, 1 <= n <= sz; where sz is the number of nodes in the list.

<br>
<br>
<br>

## Test cases

| Case                         | Input             | Output |
| ---------------------------- | ----------------- | ------ |
| Remove the last node         | [1,2,3] and n = 1 | [1,2]  |
| Remove middle node           | [1,2,3] and n = 2 | [1,3]  |
| Remove first node            | [1,2,3] and n = 3 | [2,3]  |
| Remove the only node present | [1] and n = 1     | []     |

- The above test cases seem to be complete.

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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = None
        reversed_list = self.reverseList(head)
        cur = reversed_list
        prev = None
        for i in range(1,n):
            prev = cur
            cur = cur.next
        if prev == None:
            if cur.next == None:
                pass
            else:
                res = self.reverseList(cur.next)
        else:
            prev.next = cur.next
            res = self.reverseList(reversed_list)

        return res
```

```cpp

```

<br>

#### Explanation

Reverse the list, iterate till the node to be removed and then update the prevous node's pointer to point to the current's next, then return the reveresed list.

- There are edge cases, covering the test cases will reveal all edge cases.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of nodes in the list.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Efficient solution

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

```cpp

```

<br>

#### Explanation

Utilise fast and slow pointer technique.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the size of the linked list.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Checkout [reversing a linked list](./0206-reverse-linked-list.md).

- Although it might seem that both the brute force solution and the efficient solution have the same complexity, the efficient solution is so because of the following reasons (according to LLM while I dont buy it) :
  - No reversals
  - Fewer pointer operations
  - Memory safe as things are done in place rather than temp reversal.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
