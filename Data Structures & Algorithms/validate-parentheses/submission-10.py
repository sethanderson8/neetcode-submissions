class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []

        for char in s:
            if char == '(':
                paren_stack.append(')')
            elif char == '{':
                paren_stack.append('}')
            elif char == '[':
                paren_stack.append(']')
            # this is the trickier part, need to check if paren_stack
            # is empty here and that if the char is not an opening that
            # the corresponding FILO closer is that one
            elif not paren_stack or paren_stack.pop() != char:
                return False
        # Cannot just return true here because it could just be one closing
        # char. So need to check that the stack is empty here
        return len(paren_stack) == 0 
            