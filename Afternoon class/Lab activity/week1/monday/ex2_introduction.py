CURRENT_YEAR = 2026

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
city = input("Enter your city: ")

age = CURRENT_YEAR - birth_year

print(f"\nHello, my name is {first_name} {last_name}.")
print(f"I am {age} years old and I live in {city}.")
