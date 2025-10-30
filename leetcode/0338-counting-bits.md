# Template

Easy [level question on leetcode](https://leetcode.com/problems/counting-bits/description/).

<br>
<br>
<br>

## Clarifications

- Is the input "n" always a positive integer?

  - Yes

- Can the input "n" be zero?
  - Yes, then the result will be [0]

<br>
<br>
<br>

## Test cases

| Case             | Input | Output        |
| ---------------- | ----- | ------------- |
| Positive integer | n = 5 | [0,1,1,2,1,2] |
| Zero             | n = 0 | [0]           |

<br>
<br>
<br>

## Solution

<br>
<br>

### Linearithmic solution

```py
class Solution:

    def countBits(self, n: int) -> List[int]:
        def get_num_ones(number):
            count = 0
            while number:
                #Determine if LSB is 1
                is_one = number & 1 #or number%2

                #Perform right shift
                number = number >> 1 #or number//2
                if is_one:
                    count += 1
            return count

        res = [ 0 for i in range(n+1)]

        for i in range(n+1):
            num_ones = get_num_ones(i)
            res[i] = num_ones

        return res
```

```cpp

```

<br>

#### Explanation

Loop over the bits, Determine if LSB is 1 and then keep right shifting to get the subsequent bits as LSB.

- To count the number of 1's in a number, repeatedly check if the rightmost bit is 1. Then, right shift the number to move to the next bit, and repeat this process until all bits have been checked.

<br>

#### Complexity analysis

- Time Complexity : This is a linearithmic, $O(n \times log(n))$ solution in terms of time, where $n$ is the input number.

  - Each number from 0 to $n$ is checked bit by bit. Thus the time complexity can be determined as $O(n \times k)$, where $k$ is the number of bits present in the binary representation on $n$.
  - The number of bits required to represent an integer 'i' is roughly of order [$\log_{2}(i)$](https://github.com/cybergu0ck/notes/blob/main/engineering/software/fundamentals/data-representation/number-systems/binary-system.md). Hence $k$ can be written as $\log_{2}(n)$.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is size of the result array.

<br>
<br>

### Linear dynamic programming solution

```py
class Solution:

    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        dp = [0 for i in range(n+1)]
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i//2] + (i%2)

        return dp
```

```cpp

```

<br>

#### Explanation

Solving as a 1D dynamic programming problem.

- When any number 'i' is divided by 2, the remainder will be either 0 or 1. The quotient of this division is the part which is completly divisible by 2, hence the problem has overlapping subproblems. i.e. The number of 1's in the number 'i' will be equal to the number of 1's present in the binary representation in the quotient part plus the remainder 1 if present.

1.  Define the objective function.

    $F(i)$ is the number of 1's in binary representation of number 'i'.

2.  Identify the base cases.

    - $F(0) = 0$. There are no 1's in binary representation of 0.
    - $F(1) = 1$. There is only one 1 in binary representation of 1.

3.  Form the recurrance relation.

    $$
    F(n) = F\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + (n \bmod 2)
    $$

    - $\left(\left\lfloor \frac{n}{2} \right\rfloor\right)$ is the integer division part, `n//2` in python. This is the quotient part that is completly divisible by 2.
    - $ n \bmod 2 $ is the modulo operation, `n%2` in python. This is the remainder, either 1 or 0.

4.  Find the answer.

    The whole dp array is to be returned.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is input number.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is input number, the size of the resulting array.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- LSB is the lease significant bit, typically the right most bit in the binary number.

- Determining if LSB in the binary number is 1 or 0.

  1. This can be done using bitwise AND operation on the number and value 1. i.e. `num & 1`
  1. This can be also done using [modulo operation]() and value 2. i.e. `num % 2`.
     - Modulo operation returns the remainder of the division operation. When used with value 2, we get either 1 if the number is odd and hence contains 1 in the LSB or 0 if the number is even and hence contains 0 in the LSB.
     - Modulo operation hence is also used to determine if a number is even or odd.
     - This note bridges the points of remainder of division with value 2, the LSB value and also even or odd ness of number.

* Right shifting

  - Conventionally, bitwise right shift operation.
  - Integer division by 2 is effectively equivalent to shifting the bits of the number to the right by 1 position.

- Know the usage of bitwise AND operation, bitwise right shift operation, integer division operation, modulo operation in the programming language.

- The number of bits required to represent an integer 'i' is roughly of order [$\log_{2}(i)$](https://github.com/cybergu0ck/notes/blob/main/engineering/software/fundamentals/data-representation/number-systems/binary-system.md). Hence $k$ can be written as $\log_{2}(n)$.

<br>
<br>
<br>

## Resources

- Brush up on [binary numbers](https://github.com/cybergu0ck/notes/blob/main/engineering/software/fundamentals/data-representation/number-systems/binary-system.md)

<br>
<br>
<br>
