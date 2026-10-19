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
            elif len(stack) == 0 or stack.pop() != letter:
                return False


        return len(stack) == 0