class MinStack:

    def __init__(self):
        self.Stack = []
        

    def push(self, val: int) -> None:
        self.Stack.append(val)

    def pop(self) -> None:
        self.Stack.pop()
        

    def top(self) -> int:
        if len(self.Stack) != 0:
            return self.Stack[-1]
        else: 
            return null

    def getMin(self) -> int:
        return min(self.Stack)
        
