# Average Waiting Time

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](http://rb.gy/j9g4fl).

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
  class Solution:
      def averageWaitingTime(self, customers: List[List[int]]) -> float:
          total_wait = 0
          prev_end_time = customers[0][0]

          for start_time, duration in customers:
              actual_wait_time = (prev_end_time - start_time)

              if actual_wait_time >0:
                  total_wait += (actual_wait_time + duration)
                  cur_end_time = start_time + duration + actual_wait_time
                  prev_end_time = cur_end_time
              else:
                  total_wait += duration
                  cur_end_time = start_time + duration
                  prev_end_time = cur_end_time

          return total_wait/len(customers)
  ```

  1. There are 2 test cases that I can think of.

     1. The upcoming customer's start time begins before current customer's end time, add the actual wait time plus the duration to the total wait time.
     1. The upcoming customer's start time begins after current customer's end time, add only the duration to the total time as there is no actual wait time (it is negative).

  1. Easier to come up with a logic after drawing a timeline.

     - The actual wait time for current customer is equal to (previous customer's end time - current customer's start time)
     - Current customer's wait time according to the question includes the actual wait time and the duration of the order!
     - The end time's for every customer is calculated and the previous customer's end time is continously updated.

<br>

- A similar solution, less code but needs little more thinking but based on the same logic as previous. The following has $O(n)$ time complexity $O(1)$ space complexity.

  ```py
  class Solution:
      def averageWaitingTime(self, customers: List[List[int]]) -> float:
          total_wait = 0
          cur_time = 0

          for start_time, duration in customers:
              if cur_time > start_time:
                  total_wait += cur_time - start_time
              else:
                  cur_time = start_time
              total_wait += duration
              cur_time += duration

          return total_wait/len(customers)
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

1. There are 2 test cases that I can think of.

   1. The upcoming customer's start time begins before current customer's end time.
   1. The upcoming customer's start time begins after current customer's end time.

<br>
<br>

## Resources

<br>
<br>
