# Demonstrate list constructor, remove(), and pop()

# Create a list using the list() constructor
fruits = list(("apple", "banana", "orange", "banana"))
print("Original list:", fruits)

fruits.remove("banana")  # removes the first matching item
print("After remove('banana'):", fruits)

popped = fruits.pop(1)   # removes item at index 1
print("Popped item:", popped)
print("After pop(1):", fruits)
