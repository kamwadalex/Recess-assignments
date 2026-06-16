balance = float(input("Enter starting balance: "))

while balance > 0:
  print(f"\nCurrent balance: {balance}")
  print("1. Deposit")
  print("2. Withdraw")
  choice = input("Choose an option (1-2): ")

  if choice == "1":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"Deposited {amount}. New balance: {balance}")
  elif choice == "2":
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
      print("Insufficient funds. Try a smaller amount.")
    else:
      balance -= amount
      print(f"Withdrew {amount}. New balance: {balance}")
  else:
    print("Invalid choice. Please enter 1 or 2.")

print("\nBalance is zero. you can now exit.")
