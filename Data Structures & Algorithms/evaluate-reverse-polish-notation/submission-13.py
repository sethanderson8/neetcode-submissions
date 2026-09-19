class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        currentValues = []
        ans = 0
        for i in range(0, len(tokens)):
            if tokens[i] == "*":
                currentValues.append(currentValues.pop() * currentValues.pop())
            elif tokens[i] == "/":
                a = currentValues.pop()
                b = currentValues.pop()
                currentValues.append(int(float(b) / a))
            elif tokens[i] == "+":
                currentValues.append(currentValues.pop() + currentValues.pop())
            elif tokens[i] == "-":
                a = currentValues.pop()
                b = currentValues.pop()
                currentValues.append(b - a)
            else:
                currentValues.append(int(tokens[i]))
        return currentValues.pop()
