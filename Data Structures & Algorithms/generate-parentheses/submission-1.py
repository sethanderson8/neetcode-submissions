class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        parensStack = []
        self.generateParenthesisHelper(n, parensStack, 0, 0, parens)
        return parens


    def generateParenthesisHelper(self, n, parensStack, openParen, closedParen, parens):
        if openParen == n and closedParen == n:
            parens.append("".join(parensStack))

        if openParen < n:
            parensStack.append("(")
            self.generateParenthesisHelper(n, parensStack, openParen + 1, closedParen, parens)
            parensStack.pop()

        if closedParen < openParen:
            parensStack.append(")")
            self.generateParenthesisHelper(n, parensStack, openParen, closedParen + 1, parens)
            parensStack.pop()