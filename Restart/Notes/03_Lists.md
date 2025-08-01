# Day 3 Notes: Python Lists & Dynamic Arrays

## 1. Static vs. Dynamic Arrays

A **static array** is a data structure with a **fixed size** allocated in a contiguous block of memory. Its size cannot be changed after creation.

A **dynamic array** (like a Python list) automatically resizes itself. When it becomes full, it allocates a larger block of memory and copies the old elements to the new location, hiding this complexity from the user.

---

## 2. The Resizing Process (`.append()`)

When a dynamic array runs out of space during an `append` operation, it performs these steps:
1.  A new, larger block of memory is allocated.
2.  All elements from the old block are copied to the new block (an $O(n)$ operation).
3.  The new item is added.
4.  The old block of memory is freed.

---

## 3. Amortized Analysis

This is a method for calculating the **average cost per operation** over a sequence of many operations.

For a dynamic array, the expensive $O(n)$ cost of resizing is spread out, or "amortized," over the many cheap $O(1)$ appends. This gives the `append` operation an average cost of **$O(1)$**.

---
