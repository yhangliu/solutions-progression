class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif char == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif char == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True