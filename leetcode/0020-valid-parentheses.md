# 20. Valid Parentheses

Easy [level question on leetcode](https://leetcode.com/problems/valid-parentheses/description/).

<br>
<br>
<br>

## Clarifications

<br>
<br>
<br>

## Test cases

| Case                          | Input  | Output |
| ----------------------------- | ------ | ------ |
|                               | "()"   | true   |
|                               | "([])" | true   |
| Incorrect closing parenthesis | "(]"   | false  |
| No opening parenthesis        | "]"    | false  |
| No closing parenthesis        | "["    | false  |
| Incorrect order               | "[{]}" | false  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution

```py
class Solution:
  def isValid(self, s: str) -> bool:
      opens = ('(', '{','[')
      stack = []
      for c in s:
          if c in opens:
              stack.append(c)
          elif c == ')' and stack and stack.pop() == '(':
              continue
          elif c == '}' and stack and stack.pop() == '{':
              continue
          elif c == ']' and stack and stack.pop() == '[':
              continue
          else:
              return False
      return not stack #elegant af
```

```cpp
class Solution {
public:
    bool isValid(string s) {
        std::unordered_set<char> opens = {'(', '{', '['};
        std::stack<char> stack;

        for(auto c : s){
            auto is_found = opens.find(c);
            if(is_found != opens.end())
                stack.push(c);
            else if(c == ')' && stack.size()>0 && stack.top() == '('){
                stack.pop();
            }
            else if(c == '}' && stack.size()>0 && stack.top() == '{'){
                stack.pop();
            }
            else if(c == ']' && stack.size()>0 && stack.top() == '['){
                stack.pop();
            }
            else
                return false;
        }
        return stack.empty();
    }
};
```

<br>

#### Explanation

Use a stack. Push opening parentheses, pop and validate closing ones. Return true if the stack is empty at the end.

- Iterate over the input string. If the character is an opening parenthesis, add it to the stack otherwise pop the non empty stack and check for valid closing parenthesis. At the end, return the boolean based on emptyness of the stack.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input string.
- Space Complexity : This is a linear, $O(m)$ solution in terms of space, where $m$ is number of opening parenthesis in the input string.

<br>

#### Other solutions

```py
class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"(": ")", "{":"}", "[":"]"}
        stack = []

        for c in s:
            if(c in open_to_close):
                stack.append(c)
            else:
                if(len(stack) == 0):
                    return False
                else:
                    popped = stack.pop()
                    if(open_to_close[popped] != c):
                        return False
        if(stack):
            return False
        else:
            return True
```

- The above also has the same time linear complexity.
- The above implementation is not elegant as it has multiple reutn statements and lot of branches.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

C++:

- stl stack has `push` and `pop` method to add and delete the element.
- The stack's `pop` method returns void.
- The stack has `top` method to view the top element of the stack.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
