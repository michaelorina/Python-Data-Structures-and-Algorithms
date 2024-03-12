def dequeue(self):
    if self.is_empty():
        return None
    else:
        return self.stack1.pop()