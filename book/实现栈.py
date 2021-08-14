class Stack():
    def stack(self):
        self.stack = []

    def ifEmpty(self):
        return self.stack == []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        assert not self.stack.empty()
        self.stack.pop()

    def gettop(self):
        return self.stack[-1]