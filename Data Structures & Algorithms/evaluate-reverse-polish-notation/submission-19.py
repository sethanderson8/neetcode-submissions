class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # total_sum = 0
        num_stack = deque()

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                    num_one = num_stack.pop()
                    num_two = num_stack.pop()
                    if token == "/":
                        num_stack.append(int(num_two / num_one))
                    elif token == "*":
                        num_stack.append(num_one * num_two)
                    elif token == "-":
                        num_stack.append(num_two - num_one)
                    elif token == "+":
                        num_stack.append(num_one + num_two)
            else:
                # this is where token is an int
                num_stack.append(int(token))

        return num_stack.pop()