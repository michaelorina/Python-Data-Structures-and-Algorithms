def swap_first_last(self):
    if self.head is None or self.head == self.tail:
        return
    self.head.value, self.tail.value = self.tail.value, self.head.value