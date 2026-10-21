class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # positive ->
        # negative    <-
        # abs(value) is the size of the asteroid
        # have a stack for ans_ast
        # add to stack, you only have a collision when the top of the stack
        # is positive and the one you are looking at is negative

        ans_ast = []

        for ast in asteroids:
            if ans_ast:
                # while the most recent is positive and the one we are looking at is
                # negative and bigger, keep breaking asteroids
                while ans_ast and ans_ast[-1] > 0 and ast < 0 and abs(ast) > ans_ast[-1]:
                    ans_ast.pop()
                if ans_ast and ans_ast[-1] == abs(ast) and ans_ast[-1] > 0 and ast < 0:
                    # both destroyed, pop and dont append ast
                    ans_ast.pop()
                elif not ans_ast or ans_ast[-1] < 0 and ast < 0 or ast > 0:
                    # here we append if we  see another negative and this is negative or if this is a positive
                    ans_ast.append(ast)
            else:
                ans_ast.append(ast)

        return ans_ast
