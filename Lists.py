# 🔹 1. Creating and Printing a List
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# 🔹 2. Accessing List Elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])

# 🔹 3. Modifying Lists
numbers[1] = 25
print("After modifying index 1:", numbers)

# 🔹 4. Adding and Removing Elements
numbers.append(60)
numbers.insert(2, 15)
print("After append and insert:", numbers)

numbers.remove(30)
popped = numbers.pop()
print("After remove and pop:", numbers)
print("Popped value:", popped)

# 🔹 5. Looping Through a List
print("Looping through list:")
for num in numbers:
    print(num)

# 🔹 6. List Comprehension
squares = [x * x for x in range(6)]
print("Squares using list comprehension:", squares)

# 🔹 7. Check If an Element Exists
if 25 in numbers:
    print("25 is in the list")
else:
    print("25 is not in the list")

# 🔹 8. Sorting and Reversing
numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

# 🔹 9. Basic List Functions
print("Length of list:", len(numbers))
print("Max value:", max(numbers))
print("Min value:", min(numbers))
print("Sum of elements:", sum(numbers))

# 🔹 10. Reverse a List Without reverse()
original = [1, 2, 3, 4, 5]
reversed_list = original[::-1]
print("Original list:", original)
print("Reversed copy:", reversed_list)
