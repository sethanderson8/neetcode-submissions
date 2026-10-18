class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        sum_of_scores = 0
        for op in operations:
            if op == 'D':
                sum_of_scores += (2 * scores[-1])
                scores.append(2 * scores[-1])
            elif op == '+':
                sum_of_scores +=  (scores[-1] + scores[-2])
                scores.append((scores[-1] + scores[-2]))
            elif op == 'C':
                sum_of_scores -= scores.pop()
            else:
                sum_of_scores += int(op)
                scores.append(int(op))

        return sum_of_scores