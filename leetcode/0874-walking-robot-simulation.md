# 874. Walking Robot Simulation

Medium [level question on leetcode](https://leetcode.com/problems/walking-robot-simulation/description/).

<br>
<br>
<br>

## Clarifications

No clarifications

<br>
<br>
<br>

## Test cases

| Case                       | Input                                         | Output |
| -------------------------- | --------------------------------------------- | ------ |
| No obstacles               | commands = [4,-1,3], obstacles = []           | 25     |
| With obstacles             | commands = [4,-1,4,-2,4], obstacles = [[2,4]] | 65     |
| Obstacle at starting point | commands = [6,-1,-1,6], obstacles = [[0,0]]   | 36     |

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

### Linear solution

```py
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        dirs = [[0,1], [1,0], [0,-1], [-1,0]] #In the order of N, E, S, W
        curDir = 0 #Index in dirs
        res = 0
        obstaclesSet = set(tuple(obstacle) for obstacle in obstacles)
        for command in commands:
            if command == -1:
                curDir = (curDir + 1)%4
            elif command == -2:
                curDir = (curDir - 1)%4
            else:
                dx,dy = dirs[curDir]
                for _ in range(command):
                    if (x+dx, y+dy) in obstaclesSet:
                        break
                    x = x + dx
                    y = y + dy
                res = max(res, x**2 + y**2)
        return res
```

```cpp

```

<br>

#### Explanation

Track the robot’s position and orientation by simulating each command step-by-step, checking for obstacles in a set at every move to update the peak squared distance.

- Initialise the x co-ordinate, y co-ordinate, curDir as an index in the dirs array containing directions.
- Create a set containing all the unique obstacles.
- Iterate over the commands,
  - Update the curDir if direction is to be updated.
  - Iterate over the number of steps to be moved and update x and y such that they don't coincide with an obstacle.
  - Update the result variable.

Few points to note:

- Arrange the direction vectors in clockwise order so that turning right or left corresponds to incrementing or decrementing the array index via modulo arithmetic.
- Calculate displacement by treating each direction vector as a unit vector and scaling it by the command value, which acts as the magnitude of the movement.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n + k)$ solution in terms of time, where $n$ is number of commands and $k$ is the number of obstacles.
  - The creation of set is $O(k)$.
  - The algorithm iterates over every command in the commands array, this is $O(n)$. The inner iteration is always bound as `1 <= k <= 9` (given in the question).
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is number of obstacles.

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

  - Note that `(-1%4) = 3`, i.e. This works in both directions.

<br>
<br>
<br>

## Resources

- Found this solution from [neetcode](https://www.youtube.com/watch?v=wpglWC6mnLg)

<br>
<br>
<br>
