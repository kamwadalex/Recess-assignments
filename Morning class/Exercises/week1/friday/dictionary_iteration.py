# SIMPLE DICTIONARY ITERATION EXAMPLES

student = {
    "name": "Alice",
    "age": 17,
    "grade": "11th",
    "city": "Boston"
}

# Method 1: Iterate through keys
print("--- Keys only ---")
for key in student:
    print(f"Key: {key}")

# Method 2: Iterate through values
print("\n--- Values only ---")
for value in student.values():
    print(f"Value: {value}")

# Method 3: Iterate through key-value pairs 
print("\n--- Key-Value pairs ---")
for key, value in student.items():
    print(f"{key}: {value}")

