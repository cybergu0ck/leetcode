class Solution:
    def isValid(self, s: str) -> bool:
        set = ('(', '{','[')
        stack = []
        for c in s:
            if c in set:
                stack.append(c)
            elif c == ')' and stack and stack.pop() == '(':
                continue
            elif c == '}' and stack and stack.pop() == '{':
                continue
            elif c == ']' and stack and stack.pop() == '[':
                continue
            else:
                return False
        if stack:
            return False
        return True
        return not stack