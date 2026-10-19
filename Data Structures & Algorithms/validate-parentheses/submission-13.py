class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for letter in s:
            if letter == '[':
                stack.append(']')
            elif letter == '{':
                stack.append('}')
            elif letter == '(':
                stack.append(')')
            elif not stack or stack.pop() != letter:
                return False


        return len(stack) == 0