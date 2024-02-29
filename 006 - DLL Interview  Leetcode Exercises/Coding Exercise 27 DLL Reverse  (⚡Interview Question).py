def reverse(self):
    temp = self.head
    while temp is not None:
        temp.prev, temp.next = temp.next, temp.prev
        temp = temp.prev
    self.head, self.tail == self.tail, self.head 