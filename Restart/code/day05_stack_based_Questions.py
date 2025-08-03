class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def is_valid(input_str):
    stack = Stack()
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in input_str:
        if char in bracket_map:
            top_element = stack.pop()
            if bracket_map[char] != top_element:
                return False
        else:
            stack.push(char)

    return stack.is_empty()

print(f"'()': {is_valid('()')}")
print(f"'()[]{{}}': {is_valid('()[]{}')}")
print(f"'(]': {is_valid('(]')}")
print(f"'{[()]}': {is_valid('{[()]}')}")
print(f"']': {is_valid(']')}")