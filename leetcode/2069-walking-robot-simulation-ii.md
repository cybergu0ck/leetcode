# 2069. Walking Robot Simulation II

Medium [level question on leetcode](https://leetcode.com/problems/walking-robot-simulation-ii/description/).

<br>
<br>
<br>

## Clarifications

No clarifications.

<br>
<br>
<br>

## Test cases

| Case | Input                                                                                     | Output                                                               |
| ---- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
|      | ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"] | [null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"] |
|      | [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]                                         |                                                                      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py

```

```cpp

```

<br>

#### Explanation

<!-- one line desctiption of the logic of the algorithm -->
<!-- detailed explanation with steps if appropriate -->

<br>

#### Complexity analysis

- Time Complexity : This is a <!-- time complexity in english -->, $O()$ solution in terms of time, where $ $ is <!-- placeholder -->.
- Space Complexity : This is a <!-- time complexity in english -->, $O()$ solution in terms of space, where $ $ is <!-- placeholder -->.

<br>
<br>

### Efficient solution

```py
class Robot:
    def __init__(self, width: int, height: int):
        self.array = []

        for i in range(0, width):
            self.array.append(([i,0], "East"))

        for i in range(1, height):
            self.array.append(([width-1,i], "North"))

        for i in range(width-2,-1,-1):
            self.array.append(([i, height-1], "West"))

        for i in range(height-2, 0, -1):
            self.array.append(([0, i], "South"))

        self.curIndex = 0
        self.hasMoved = False

    def step(self, num: int) -> None:
        self.hasMoved = True
        self.curIndex = (self.curIndex + num) % len(self.array)

    def getPos(self) -> List[int]:
        return self.array[self.curIndex][0]

    def getDir(self) -> str:
        if self.hasMoved and self.curIndex == 0:
            return "South"
        else:
            return self.array[self.curIndex][1]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
```

```cpp

```

<br>

#### Explanation

The robot can move only in the boundary cells and the direction of the robot in a specific cell is also fixed.

- Create a 1D array containing all boundary cell coordinates in sequence, paired with the fixed direction assigned to each cell.
  - This 1D array effectively represents the circular boundary "unrolled" into a linear format.
- Use a single variable to track the robot's current index within this 1D array.
- For each move command, update the current index using modular arithmetic to account for the cyclic nature of the boundary.
- Retrieve the robot's current position and direction directly from the array using the current index.

Note that there is one edge case that needs to be taken care of :

- The robot begins at the first cell $(0,0)$ facing "East". However, if the robot completes a lap and returns to $(0,0)$, its direction must be "South".
- This is handled by tracking whether the robot has moved at least once. If the robot is at index $0$ and the movement flag is true, the direction is returned as "South" instead of the initial "East".

<br>

#### Complexity analysis

- Time Complexity :
  1. Initialisation : This is a linear, $O(w+h)$ solution in terms of time, where $w$ is the width and $h$ is the height.
     - The total work is proportional to the perimeter of the grid: $2 \times (W + H)$. In Big O notation, we drop constants, resulting in $O(W + H)$.
  1. Stepping : This is constant time.
  1. Getting position : This is constant time.
  1. Getting direction : This is constant time.

<br>

- Space Complexity : This is a linear, $O(w+h)$ solution in terms of space, where $w$ is the width and $h$ is the height.
  - The class stores every coordinate on the perimeter of the rectangle within self.array.
  * Total elements $\approx 2W + 2H - 4$.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Modulo operator gives the remainder value.

- Use the modulo operator to map an out-of-bounds index back into the valid range of an array, allowing for seamless circular traversal.

  ```py
  nums = [10,20,30]
  # To treat index 3 as index 0, or index 4 as index 1:
  newIndex = 3 % (len(nums)) #0
  ```

<br>
<br>
<br>

## Resources

- Got this clever solution from youtube.

<br>
<br>
<br>
