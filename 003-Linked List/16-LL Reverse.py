def reverse(self):
    temp = self.head 
    self.head = self.tail 
    self.tail = temp 

    after = temp.next
    before = None

    for _ in range(self.length):
        after = temp.next
        temp.next = before 
        before = temp
        temp = after 
         