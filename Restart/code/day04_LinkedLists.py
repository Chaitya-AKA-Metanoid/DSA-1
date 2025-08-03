class Node:
    def __init__(self, data):
        self.next = None  # Points to the next node
        self.data = data  # Stores the data

class LinkedList:
    
    def __init__(self):
        self.head = None  # Start with an empty list

    def display(self):
        current = self.head
        while current != None:
            # If there's a next node, print the node's data followed by "->"
            if current.next:
                print(current.data, "->", end=" ")
            else:
                print(current.data)  # Print the last node without "->"
            current = current.next  # Move to the next node

    def delete(self, key): 
        current = self.head
        
        if self.head == None:  # If the list is empty
            print("The list is empty!")
            return 
        
        # Case: Delete the head node if it matches the key
        if self.head.data == key:
            self.head = self.head.next  # Move head to the next node
            return
        
        # Case: Traverse the list and find the node to delete
        prev = None
        current = self.head
        while current and current.data != key:  # Traverse until we find the key or reach the end
            prev = current  # Keep track of the previous node
            current = current.next  # Move to the next node

        # Case: If the node is found
        if current:  # Node found
            prev.next = current.next  # Bypass the node to delete it
            current = None  # Optional: break the reference to the deleted node
        else:
            print(f"Node with data {key} not found.")  # Node not found in the list

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head == None:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Append the new node to the end of the list

# --- Test Your Code ---
my_list = LinkedList()

# 1. Append nodes
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Initial list:")
my_list.display()

# 2. Delete a node from the middle
print("\nDeleting 20...")
my_list.delete(20)
my_list.display()

# 3. Delete the head node
print("\nDeleting the head (10)...")
my_list.delete(10)
my_list.display()

# 4. Delete the tail node
print("\nDeleting the tail (40)...")
my_list.delete(40)
my_list.display()

# 5. Try to delete a node that doesn't exist
print("\nTrying to delete 99...")
my_list.delete(99)
my_list.display()