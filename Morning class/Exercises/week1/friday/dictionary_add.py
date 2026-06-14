# Adding items to a dictionary

student = {}

# Method 1: Direct assignment (add new key-value pair)
student["name"] = "John"
student["age"] = 16
print("After adding name and age:")
print(student)

# Method 2: Using update() method
student.update({"grade": "10th"})
student.update({"city": "New York"})
print("\nAfter update method:")
print(student)
