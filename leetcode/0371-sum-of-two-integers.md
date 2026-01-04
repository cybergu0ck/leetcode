# Template

Medium [level question on leetcode](https://leetcode.com/problems/sum-of-two-integers/description/).

<br>
<br>
<br>

## Clarifications

- What kind of numbers are a and b?
  - a and b are integers with the range -1000 <= a, b <= 1000.

<br>
<br>
<br>

## Test cases

| Case                           | Input          | Output |
| ------------------------------ | -------------- | ------ |
| Both positive integers         | a = 2, b = 3   | 5      |
| Both negative integers         | a = -2, b = -3 | -5     |
| Positive and Negative integers | a = 2, b = -3  | -1     |
| Large Positive integers        | a = 20, b = 30 | 50     |
| One and minus one              | a = 1, b = -1  | 0      |

- Initially I did not include the following test cases and the developed algorithm passed the test cases at the time and later found that the solution is error prone :

  1. Large positive integers : Sometimes the smaller binary numbers hide away the deeper insight
  1. One and minus one : Special case specifically for Python. Python allows of integer overflow and is not bound to any number of bits (like 32 bits or something). -1 in Python is string of infinite 1's. Adding 1 and -1 will create infinite ripple of carry's!

<br>
<br>
<br>

## Solution

<br>
<br>

### Constant time solution

```py
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        # Handle the 32-bit signed integer range
        return (a & mask) if b > 0 else a
```

```cpp

```

<br>

#### Explanation

Use bitwise operators and a mask.

- Bitwise AND operation results in 1 only if both corresponding bits are 1.
  - If the AND operation of two bits yields a 1, then the value at that bit must be added twice for the calculation of addition.
  - Shifting a bit left by 1 is basically the addition of the previous bit by itself. Example : `0010` is decimal 2, `0100` is decimal 4 (which is 2 added twice).
- Bitwise XOR operation results only if the bits are different (one bit is 1 and the other is 0).
- All the bits in these two results `(a&b) << 1)` and `a^b` when taken into account will yield the result of addition value. An AND or OR opeation cannot be performed on these two resuls to derive the expected result, if both bits are 1, OR operation will take into account account only once but we need to take both into account. So we need to continously check if carry is being generated, if it is we keep repeating the process until there is no carry.

* Use mask for Python

  - The mask must be used for languages like Python where integer overflow is allowed. `0xFFFFFFFF` is 32 bits of 1. When used along with an AND operator, it retains only 32 bits by chopping off the remaining bits. Left shift operation is not limited to any number of bits in Python as it keeps the bits overflowing. Essentially the while loop condition is checking if the 32 bits of the carry generated has any repeated 1's.

  - The return is not straight forward because there might be carry generated after the 32'nd bit. The while loop condition doesn't check that. If a carry is generated after 32 nd bit, it means it is a neagative number and it'll be a huge negative integer in Python. If so, we need to consider only 32 bits (chop off the extra bits using the mask).

<br>

#### Complexity analysis

- Time Complexity : This is a constant, $O(1)$ solution in terms of time.

  - The while loop runs based on the carry. Every time `carry = (a & b) << 1` is performed. Since we are simulating a 32-bit integer (enforced by the mask), the carry can only shift left a maximum of 32 times before it falls off the edge and becomes zero.

- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

- //TODO - Instead of considering the 32 bit range in the while loop condition in Python solution, can we try actually chopping off the rest and just keeping 32 bits?

<br>
<br>
<br>

## Notes

- Understand usage of bitwise operators in the language.
- Left shifting by 1 means adding the value at previous bit twice.
- `0xFFFFFFFF` is 32 bits of 1.
- Integers overflow in Python, utilize a mask to consider 32 bit range.
- -1 in Python is represented as an infinite string of 1! Hence always consider a test case for it. In this case a=-1 and b=1. When 1 is added to -1, the carry bit creates an infinite ripple!

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
