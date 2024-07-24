# Sort the Jumbled Numbers

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/sort-the-jumbled-numbers/description/).

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

1. Encoding is done sing a list.

   ```py
   class Solution:
       def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
           pairs = []

           for index,num in enumerate(nums):
               text = str(num)
               encoded_list = []
               for char in text:
                   encoded_digit = str(mapping[int(char)])
                   encoded_list.append(encoded_digit)
               encoded_text = ''.join(encoded_list)
               encoded_num = int(encoded_text)
               pairs.append((encoded_num, index))

           pairs.sort() #python's sort will sort based on first value of the tuple, it'll choose second value in case of tie
           return [ nums[item[1]] for item in pairs]
   ```

2. Encoding is done directly using a integer, no array is used (better).

   ```py
   class Solution:
     def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
         pairs = []

         for index,num in enumerate(nums):
             text = str(num)
             encoded_num = 0
             for char in text:
                 encoded_num *= 10
                 encoded_num += mapping[int(char)]
             pairs.append((encoded_num, index))

         pairs.sort() #python's sort will sort based on first value of the tuple, it'll choose second value in case of tie
         return [ nums[item[1]] for item in pairs]
   ```

3. Using more math for more efficiency.

   ```py
   class Solution:
       def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
           pairs = []

           for index,num in enumerate(nums):
               encoded_num = 0
               if num == 0:
                   encoded_num = mapping[num]
               base = 1
               while num >0:
                   units_digit = num % 10   #This will get the unit's place digit
                   num = num//10   #This will chuck away the unit's place digit
                   encoded_num += base * mapping[units_digit]
                   base *= 10
               pairs.append((encoded_num, index))

           pairs.sort() #python's sort will sort based on first value of the tuple, it'll choose second value in case of tie
           return [ nums[item[1]] for item in pairs]
   ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- Python list's sort method, specifically when the items are tuples, sorts the tuples based on the first value. It will automatically consider second value if there is a tie.

  ```py
  pairs = [(1,2), (2,4), (1,1)]
  pairs.sort()
  print(pairs)

  #[(1, 1), (1, 2), (2, 4)]
  ```

- The time complexity for the below code is $O(d)$, where d is the number of digits.

  ```py
  number = 123
  text = str(number) #O(n)
  ```

- The unit's place digit of an integer is given by

  ```py
  number = 123
  print(number % 10)
  #3
  ```

- The number without the unit's place is given by

  ```py
  number = 123
  print(number // 10)
  #12
  ```

<br>
<br>

## Test Cases

- Test cases doesnt play a major role for finding solution.

<br>
<br>

## Resources

<br>
<br>
