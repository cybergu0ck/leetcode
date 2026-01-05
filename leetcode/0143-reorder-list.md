# Template

Medium [level question on leetcode](https://leetcode.com/problems/reorder-list/description/).

<br>
<br>
<br>

## Clarifications

- Is the given head always valid?
  - The number of nodes in the list is in the range [1, 5 * 104].

<br>
<br>
<br>

## Test cases

| Case                        | Input     | Output    |
| --------------------------- | --------- | --------- |
| Linked list with Even nodes | 1,2,3,4   | 1,4,2,3   |
| Linked list with Odd nodes  | 1,2,3,4,5 | 1,5,2,4,3 |
| Linked list with One nodes  | 1         | 1         |
| Linked list with Two nodes  | 1,2       | 1,2       |

<br>
<br>
<br>

## Solution

<br>
<br>

### Quadratic solution

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        while cur.next:
            cur.next = self.reverseList(cur.next)
            cur = cur.next
        return head
```

```cpp

```

<br>

#### Explanation

Repeatedly reverse the reamining tail nodes, simultaneously updating the sorted portion.

- For every node `cur`, it takes the entire remaining portion of the list (`cur.next`) and reverses it completely.

- By reversing the tail at every step, the original "last" node of the current tail constantly becomes the "next" node for cur.

<br>

#### Complexity analysis

- Time Complexity : This is a Quadratic, $O(n^2)$ solution in terms of time, where $n$ is number of nodes in the linked list.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Linear solution

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def getMiddleNode(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        firstList = head
        middleNode = self.getMiddleNode(head)
        secondList = self.reverseList(middleNode.next)
        middleNode.next = None

        cur = head
        firstList = firstList.next
        toggle = False
        while firstList and secondList:
            if toggle:
                cur.next = firstList
                firstList = firstList.next
            else:
                cur.next = secondList
                secondList = secondList.next
            cur = cur.next
            toggle = not toggle

        if firstList:
            cur.next = firstList
        if secondList:
            cur.next = secondList
```

```cpp

```

<br>

#### Explanation

Split the linked list in half, reverse the second half and insert the nodes from the two splits alternatingly.

- Use slow and fast pointer approach to find the middle node of a linked list.
- Split the given linked list at the middle node, such that the second half is `middleNode.next`.
- Reverse the second half.
- Merge by adding nodes from the two splits alternatively.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of nodes in the linked list.
  - The algorithm to get the middle node is $O(n)$.
  - The algorithm to reverse a linked list is $O(n)$.
  - The algorithm of alternating merge is also $O(n)$, as each node is visited only once.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Linear elegant solution

A refined merge logic is as follows :

```py
# Instead of the toggle loop:
while secondList:
    # Save the next nodes
    tmp1, tmp2 = firstList.next, secondList.next

    # Re-wire the pointers
    firstList.next = secondList
    secondList.next = tmp1

    # Move pointers forward
    firstList, secondList = tmp1, tmp2
```

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Know how to reverse a linked list
- Know how to get the middle node of a linked list using slow and fast pointer approach.
- Know how to perform an alternating merge from two linked lists.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
