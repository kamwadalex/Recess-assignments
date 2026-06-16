message = "I am global"


def show_global():
  print("Inside function (reading global):", message)


def try_change_local():
  message = "I am local"
  print("Inside function (local variable):", message)


def change_global():
  global message
  message = "Global was changed"


print("Before function calls:", message)
show_global()
try_change_local()
print("After local assignment in function:", message)
change_global()
print("After global keyword in function:", message)
