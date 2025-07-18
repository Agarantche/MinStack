class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.main_stack:
            popped_val = self.main_stack.pop()
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]
        # According to constraints, pop, top and getMin will always be called on non-empty stacks,
        # so we don't strictly need to handle an empty main_stack here, but good practice.
        return None 

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        # According to constraints, pop, top and getMin will always be called on non-empty stacks.
        return None
