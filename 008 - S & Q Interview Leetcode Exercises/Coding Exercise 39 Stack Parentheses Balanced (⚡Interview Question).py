def is_balanced_parenteses(parenteses):
    stack = Stack()
    for p in parenteses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()