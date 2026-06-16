def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b


def get_number(prompt):
  while True:
    value = input(prompt)
    try:
      return float(value)
    except ValueError:
      print("Please enter a valid number.")


def show_menu():
  print("\n--- Calculator ---")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")


def main():
  operations = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
  }

  while True:
    show_menu()
    choice = input("Choose an operation (1-5): ").strip()

    if choice == "5":
      print("Goodbye!")
      break

    if choice not in operations:
      print("Invalid choice. Try again.")
      continue

    name, operation = operations[choice]
    first = get_number("Enter first number: ")
    second = get_number("Enter second number: ")

    try:
      result = operation(first, second)
      print(f"Result: {first} {name.lower()} {second} = {result}")
    except ValueError as error:
      print(f"Error: {error}")


if __name__ == "__main__":
  main()
