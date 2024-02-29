def swap_pairs(self):
    dummy = Node(0)
    dummy.next = self.head 
    prev = dummy

    while self.head and self.head.next:
        first_node = self.head
        second_node = self.head.next

        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        second_node.prev = prev
        first_node.prev = second_node
        if first_node.next:
            first_node.next.prev = first_node
        
        self.head = first_node.next
        prev = first_node
    
    self.head = dummy.next