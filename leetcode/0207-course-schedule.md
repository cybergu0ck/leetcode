# 207. Course Schedule

Medium [level question on leetcode](https://leetcode.com/problems/course-schedule/description/).

<br>
<br>
<br>

## Clarifications

No clarifications.

<br>
<br>
<br>

## Test cases

| Case                     | Input                                         | Output |
| ------------------------ | --------------------------------------------- | ------ |
| No prerequsities         | numCourses = 2, prerequisites = []            | True   |
| All courses tackable     | numCourses = 2, prerequisites = [[1,0]]       | True   |
| All courses not tackable | numCourses = 2, prerequisites = [[1,0],[0,1]] | False  |

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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        courseToPrerequsite = defaultdict(list)

        for item in prerequisites:
            courseToPrerequsite[item[0]].append(item[1])

        courseTackable = set()
        def rec(course, visited):
            if course not in courseToPrerequsite or course in courseTackable:
                return True
            prereqs = courseToPrerequsite[course]
            if course in visited:
                return False
            visited.add(course)
            for item in prereqs:
                if not rec(item, visited):
                    return False
            visited.remove(course)  #Cruical
            courseTackable.add(course)
            return True

        for course in courseToPrerequsite:
            visited = set()
            if not rec(course, visited):
                return False

        return True
```

```cpp

```

<br>

#### Explanation

Use Memoised DFS on the adjacency map.

- Create a map with keys as courses and values as list of prerequsites for that course.
- Use a set to keep track of cycles.
- For every course in the map, run the recursive function (DFS).
- Memoize the algorithm by keeping track of computed results.

Points to note:

- While backstepping in recursion, `visited` set needs to updated correctly by removing the course.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(E)$ solution in terms of time, where $E$ is the number of prerequsites.
  - Creating the `courseToPrerequsite` map is $O(E)$.
  - For each item in `courseToPrerequsite` map, the recursive function is called which in the worst case can run E times i.e. $O(E^2)$. However, Memoisation is used here using `courseTackable` hence the recursive function is run once per course in the `courseToPrerequsite`. Therefore this is $O(E)$.
  - Hence, overall it is $O(E)$.

<br>

- Space Complexity : This is a linear, $O(V+E)$ solution in terms of space, where $V$ is the number of courses and $E$ is the number of prerequsites.
  - Creating the `courseToPrerequsite` map is $O(E)$.
  - Using `courseTackable` for memoization is $O(V)$, it can keep track of any course from the available courses.
  - Hence, overall it is $O(V+E)$.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
