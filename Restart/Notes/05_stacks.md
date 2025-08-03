1. Core Concept: LIFO
A stack is a linear data structure that adheres to the LIFO (Last-In, First-Out) principle. This dictates that the last element to be added to the stack is the first element to be removed. All insertion and deletion operations occur at the same end of the stack, referred to as the "top".

---
## 2. Core Operations
A stack is primarily defined by three fundamental operations, all of which have a time complexity of **$O(1)$**.

push(item): Adds a new element to the top of the stack. This operation modifies the stack by increasing its size by one.

pop(): Removes and returns the element currently at the top of the stack. This operation modifies the stack by decreasing its size by one. Attempting to `pop` from an empty stack results in an **underflow error**.

`peek()`: Returns the element at the top of the stack **without** removing it. This is a read-only operation and does not modify the stack.

---
3. Implementation
Stacks are commonly implemented using either a **dynamic array** (like a Python `list`) or a **singly linked list** as the underlying data structure.