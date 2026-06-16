# Nested dictionary

# Example 1: Student with subjects and grades
student = {
    "name": "Bob",
    "age": 16,
    "subjects": {              
        "math": 85,
        "science": 90,
        "english": 78
    }
}

print("--- Accessing nested data ---")
print(f"Student: {student['name']}")
print(f"Math grade: {student['subjects']['math']}")
print(f"Science grade: {student['subjects']['science']}")

# Iterate through nested dictionary
print("\n--- All subjects and grades ---")
for subject, grade in student['subjects'].items():
    print(f"{subject}: {grade}")