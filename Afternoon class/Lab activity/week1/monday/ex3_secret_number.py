secret_number = int(input("Enter the secret number: "))
attempts = 3

for attempt in range(1, attempts + 1):
  guess = int(input(f"Attempt {attempt} of {attempts} - Enter your guess: "))

  if guess == secret_number:
    print(f"\nCorrect! The secret number is {secret_number}.")
    break
  else:
    print("Wrong guess.")
else:
  print(f"\nOut of attempts. The correct number was {secret_number}.")
