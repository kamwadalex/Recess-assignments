# Assignment 1: Bill Split Calculator
# Calculates tip, total, and per-person share with formatted receipt output


def get_positive_float(prompt):
    """Ask for a positive number with validation."""
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number <= 0:
                print("Please enter a number greater than zero.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_int(prompt):
    """Ask for a positive whole number with validation."""
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number <= 0:
                print("Please enter a whole number greater than zero.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_tip_percentage():
    """Ask user to choose a tip percentage (10%, 15%, 20%, or custom)."""
    print("\nTip options:")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    print("4. Custom")

    preset_tips = {"1": 10, "2": 15, "3": 20}

    while True:
        choice = input("Select tip option (1-4): ").strip()

        if choice in preset_tips:
            return preset_tips[choice]

        if choice == "4":
            while True:
                custom = input("Enter custom tip percentage (e.g. 18): ").strip()
                try:
                    tip = float(custom)
                    if tip < 0:
                        print("Tip percentage cannot be negative.")
                        continue
                    return tip
                except ValueError:
                    print("Invalid input. Please enter a valid percentage.")

        print("Invalid choice. Please enter 1, 2, 3, or 4.")


def format_currency(amount):
    """Format amount in Ugandan Shillings."""
    return f"USh {amount:,.0f}"


def print_receipt(bill_amount, tip_percent, tip_amount, total_amount, num_people, per_person):
    """Print a formatted receipt with all calculations."""
    width = 42
    line = "=" * width

    print(f"\n{line}")
    print(f"{'BILL SPLIT RECEIPT':^{width}}")
    print(line)
    print(f"{'Original bill:':<22}{format_currency(bill_amount):>20}")
    print(f"{'Tip (' + str(tip_percent).rstrip('0').rstrip('.') + '%):':<22}{format_currency(tip_amount):>20}")
    print(f"{'-' * width}")
    print(f"{'Total (bill + tip):':<22}{format_currency(total_amount):>20}")
    print(f"{'Number of people:':<22}{num_people:>20}")
    print(f"{'Amount per person:':<22}{format_currency(per_person):>20}")
    print(line)


def main():
    print("=" * 42)
    print("       BILL SPLIT CALCULATOR")
    print("=" * 42)

    bill_amount = get_positive_float("\nEnter total bill amount (USh): ")
    num_people = get_positive_int("Enter number of people: ")
    tip_percent = get_tip_percentage()

    tip_amount = bill_amount * (tip_percent / 100)
    total_amount = bill_amount + tip_amount
    per_person = total_amount / num_people

    print_receipt(bill_amount, tip_percent, tip_amount, total_amount, num_people, per_person)


if __name__ == "__main__":
    main()
