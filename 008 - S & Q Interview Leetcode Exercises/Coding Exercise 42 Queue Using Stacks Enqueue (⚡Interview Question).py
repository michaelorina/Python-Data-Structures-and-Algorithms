def enqueue(self, value):
    while len(self.stack) > 0:
        self.stack2.append(self.stack1.pop())
    self.stack1.append(value)
    while len(self.stack2) > 0:
        self.stack1.append(self.stack2.pop())