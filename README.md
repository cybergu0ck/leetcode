# Readme

<br>

[Tracker](https://docs.google.com/spreadsheets/d/1DO9uZ4bku1E6rTBiuodk3nMoZSRfDQLyuXbjgwlqC7k/edit?gid=1977686793#gid=1977686793)

<br>
<br>
<br>

## Process of solving a leetcode question

1. Read the question.
   - Read the question complemently.
   - Understand what is needed to be done?
   - Something to be returned or done in place?
1. Confirm understanding.
   - Pick a simple example case and write down the expected outcome and confirm if the understanding is correct.
1. Ask clarification questions.
1. Prepare test cases.
1. Come up with brute force solution.
1. Develop an optimised solution.

<br>
<br>
<br>

## Array based questions

<br>
<br>

### Typical clarification questions

1. Is the array sorted?

1. Is the array comprised of unique elements?

1. What is the type of data stored in the array?
   - If the data type is integers, then it contains positive, negative and zeros.

1. Can the array be modified?
   - If the question demands "in-place" logic, it means array must be modified.

1. Can the array be empty?

<br>
<br>

### Test cases

| Case                         | Array     |
| ---------------------------- | --------- |
| Empty Array                  | []        |
| Array with single element    | [100]     |
| Array with positive elements | [1,2,3]   |
| Array with dupliates         | [1,2,2,4] |
| Array with polarity          | [-1,0,1]  |

<br>
<br>
<br>

## Matrix based questions

Matrix is typically a 2D array.

<br>
<br>

### Typical clarification questions

1. What is the minimum and maximum dimensions of the givem `m*n` matrix?
   - Example answer: `1 <= m, n <= 200`

1. Any input constraints on the element, data type and values?
   - Example answer: `-2^31 <= matrix[i][j] <= 2^31 - 1`

1. Do we have the liberty to modify the type and value of the elements?
   - Example answer: Matrix must contain integer types, values can be modified.

1. Can the matrix be empty?
   - Example answer: No, at the very least matrix contains only 1 cell.

<br>
<br>

### Test cases

| Case | Matrix |
| ---- | ------ |

<br>
<br>
<br>
