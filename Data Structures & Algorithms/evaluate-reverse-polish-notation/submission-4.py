class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        given:
        - reverse polish notation
        - treat division as int division
        asked:
        - evaluate
        return:
        - evaluation
        constraints:
        -nothing
        sol:
        - using stack, keep on popping and evaluation expr
        """

        st = []
        for token in tokens:
            op = token
            if op not in "+-*/":
                st.append(int(op))
            else:
                op2 = st.pop()
                op1 = st.pop()
                res = 0
                if op == "+":
                    res = op1 + op2
                elif op == "-":
                    res = op1 - op2
                elif op == "*":
                    res = op1 * op2
                elif op == "/":
                    res = int(op1 / op2)
                else:
                    # should not come here
                    pass
                st.append(res)
        
        return st[-1]
