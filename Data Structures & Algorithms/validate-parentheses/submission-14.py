class Solution:
    def isValid(self, s: str) -> bool:
        paren_pairs = {'(': ')', '{': '}', '[': ']'}
        paren_stack = deque()

        for c in s:
            if c in paren_pairs:
                paren_stack.append(c)
            else:
                if paren_stack and paren_pairs[paren_stack[-1]] == c:
                    paren_stack.pop()
                else:
                    return False

        return not paren_stack