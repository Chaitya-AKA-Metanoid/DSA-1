class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # Always use 'self.items' to refer to the instance's list
        self.items.append(item)
        # Push operations typically don't return anything

    def pop(self):
        # Call methods with 'self.is_empty()'
        if not self.is_empty():
            # .pop() removes and returns the last item
            return self.items.pop()
        else:
            print("Error: Stack is empty")
            return None # Return None on failure

    def peek(self):
        if not self.is_empty():
            # Return the last item without removing it
            return self.items[-1]
        else:
            print("Error: Stack is empty")
            return None # Return None on failure

    def is_empty(self):
        # This can be simplified to a single line
        return len(self.items) == 0

    def size(self):
        # This method should return the size, not print it
        return len(self.items)
    
# --- Test Your Code ---
s = Stack()
print(f"Is stack empty? {s.is_empty()}") # Expected: True

s.push(10)
s.push(20)
print(f"Stack size: {s.size()}") # Expected: 2
print(f"Peek: {s.peek()}") # Expected: 20

popped_item = s.pop()
print(f"Popped item: {popped_item}") # Expected: 20
print(f"Peek after pop: {s.peek()}") # Expected: 10
