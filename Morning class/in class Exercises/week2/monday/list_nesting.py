# Demonstrate nesting in lists
students = [
    ["John", 16, "10th"],
    ["Mary", 15, "9th"],
    ["Peter", 17, "11th"]
]

print(students)
print(students[0])        # first inner list
print(students[1][0])     # name from second inner list

for student in students:
    print(student[0], student[1], student[2])
