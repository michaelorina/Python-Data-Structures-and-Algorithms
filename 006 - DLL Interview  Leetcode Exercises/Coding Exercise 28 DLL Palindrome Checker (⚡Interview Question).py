def is_palindrome(self):
    if self.length <= 1:
        return True
    forward_node = self.head
    backward_node = self.tail
    for i in range(self.length // 2):
        if forward_node.value != backward_node.value:
            return False
        forward_node = forward_node.next
        backward_node = backward_node.prev
    return True