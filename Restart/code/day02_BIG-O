import math

# O(n) example – Linear Time
def linear():
    print("\nExample of O(n) time: ")
    data = [1, 2, 3, 4, 5, 6]
    for i in data:
        if i == 3:
            print("Found target in O(n) time by linear search")

# O(1) example – Constant Time
def constant():
    print("\nExample of O(1) time: ")
    data = [1, 2, 3, 4, 5, 6]
    answer = data[3]  # Direct access
    print("O(1) result:", answer)
    print("Used direct access for O(1)")
# O(n^2) example – Quadratic Time
def quadratic():
    print("\nExample of O(n^2) time: \n")
    print("Printing a pattern using nested loops")
    for i in range(1, 6):
        for k in range(1, i + 1):
            print(k, end='')
        print()

# O(log n) example – Binary Search
def logn():
    print("\nExample of O(log(n)) time: Binary search")
    target = 82
    data = [5, 7, 14, 30, 82, 99]
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_value = data[middle]

        if target == middle_value:
            print("Found in O(log n) time at index", middle)
            return
        elif target < middle_value:
            high = middle - 1
        else:  # target > middle_value
            low = middle + 1

    print("Target not found")

#O (nlogn) time complexity using anagrams 
def nlogn():
    print("\nExample of O(nlogn) time:")
    str1 = 'Hello'
    str2 = 'olleH'
    # Quick length check to fail fast
    if len(str1) != len(str2):
        print("These are not anagrams")

    # Sort and compare
    if sorted(str1) == sorted(str2):
        print("These are anagrams")
    else :
        print("These are not anagrams")


# Run all
linear()
constant()
quadratic()
logn()
nlogn()