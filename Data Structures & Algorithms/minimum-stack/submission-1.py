class MinStack:

    def __init__(self):
        self.st = [float('inf')]
        self.vals = []
        

    def push(self, val: int) -> None:
        self.vals.append(val)
        self.st.append(min(self.st[-1], val))
        

    def pop(self) -> None:
        if(not self.vals):
            return

        self.vals.pop()
        self.st.pop()
        

    def top(self) -> int:
        if not self.vals:
            return None
        return self.vals[-1]
        

    def getMin(self) -> int:
        if not self.vals:
            return None
        return self.st[-1]
        

        """
        given:
        - empty stack
        - input is any signed int
        asked:
        - min at each element level
        constraint:
        - more 30K calls
        sol:
        - using stack keep min at each level
        """