def sort_stack(stack):
    additional_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()

        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())
        
        additional_stack.push(temp)

    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())