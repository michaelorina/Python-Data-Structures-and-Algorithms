def partition_list(self, x):
        if not self.head:
            return None
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        
        prev2.next = None
        prev1.next = dummy2.next
        
        self.head = dummy1.next