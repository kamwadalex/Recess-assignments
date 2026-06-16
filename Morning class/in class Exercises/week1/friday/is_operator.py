x = 10
y = 10
z = x

print(x is z)   # True (same object)
print(x is y)   # True (Python caches small integers)
print(x == y)   # True (same value)

# For strings 
name1 = "hello"
name2 = "hello"
print(name1 is name2)   # True (Python interns strings sometimes)

# Example
result = None
if result is None:
    print("No result yet")


# Example

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Check same object in memory
if a is c:
    print("a and c are the same object")

if a is not b:
    print("a and b are different objects (even though they have same values)")

# Compare with == 
print(a == b)   # True (same values)
print(a is b)   # False (different objects)
print(a is c)   # True (same object)