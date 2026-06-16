# Real world application using control structures
# Assignment 2: E-commerce platform with login, coupons, tax, and role-based access

USERS = {
    "admin": {"password": "admin123", "role": "admin", "name": "System Admin"},
    "amina": {"password": "shop456", "role": "customer", "name": "Amina Namukasa"},
    "brian": {"password": "buy789", "role": "customer", "name": "Brian Okello"},
    "cashier1": {"password": "pos111", "role": "cashier", "name": "Constance Akello"},
    "cashier2": {"password": "pos222", "role": "cashier", "name": "David Mugisha"},
}

COUPONS = {
    "WELCOME10": {"type": "percent", "value": 10, "min_subtotal": 0},
    "SAVE15": {"type": "percent", "value": 15, "min_subtotal": 50000},
    "BIG25": {"type": "percent", "value": 25, "min_subtotal": 100000},
    "FLAT10K": {"type": "flat", "value": 10000, "min_subtotal": 30000},
    "VIP50K": {"type": "flat", "value": 50000, "min_subtotal": 200000},
}

TAX_RATES = {
    "kampala": 0.18,
    "entebbe": 0.18,
    "jinja": 0.18,
    "mbarara": 0.18,
    "gulu": 0.18,
    "wakiso": 0.18,
}

DEFAULT_TAX_RATE = 0.18


def format_ugx(amount):
    """Format amount in Ugandan Shillings."""
    return f"USh {amount:,.0f}"


def login():
    """Authenticate user credentials and return user info or None."""
    print("\n--- LOGIN ---")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    if username in USERS:
        user = USERS[username]
        if user["password"] == password:
            print(f"\nWelcome, {user['name']}!")
            if user["role"] == "admin":
                print("Access level: FULL (Admin)")
            elif user["role"] == "cashier":
                print("Access level: CASHIER (Process sales)")
            elif user["role"] == "customer":
                print("Access level: CUSTOMER (Shop & checkout)")
            return {"username": username, **user}
        else:
            print("Invalid password.")
    else:
        print("Username not found.")

    return None


def get_volume_discount_rate(subtotal):
    """Return extra discount percent based on subtotal tiers."""
    if subtotal >= 200000:
        return 0.15, f"15% volume discount (orders {format_ugx(200000)}+)"
    elif subtotal >= 100000:
        return 0.10, f"10% volume discount (orders {format_ugx(100000)}+)"
    elif subtotal >= 50000:
        return 0.05, f"5% volume discount (orders {format_ugx(50000)}+)"
    else:
        return 0.0, "No volume discount"


def apply_coupon(subtotal, coupon_code):
    """Validate coupon and return discount amount with nested conditions."""
    coupon_code = coupon_code.strip().upper()

    if not coupon_code or coupon_code == "NONE":
        return 0.0, "No coupon applied"

    if coupon_code in COUPONS:
        coupon = COUPONS[coupon_code]
        if subtotal >= coupon["min_subtotal"]:
            if coupon["type"] == "percent":
                discount = subtotal * (coupon["value"] / 100)
                return discount, f"Coupon {coupon_code}: {coupon['value']}% off"
            elif coupon["type"] == "flat":
                discount = min(coupon["value"], subtotal)
                return discount, f"Coupon {coupon_code}: {format_ugx(coupon['value'])} off"
        else:
            return 0.0, (
                f"Coupon {coupon_code} requires minimum subtotal "
                f"of {format_ugx(coupon['min_subtotal'])}"
            )
    else:
        return 0.0, f"Invalid coupon code: {coupon_code}"


def get_tax_rate(location):
    """Return tax rate based on location using nested conditions."""
    location = location.strip().lower().replace(" ", "_")

    if location in TAX_RATES:
        rate = TAX_RATES[location]
        return rate, f"VAT for {location.replace('_', ' ').title()}: {rate * 100:.0f}%"
    elif location in ("export", "tourist_refund"):
        return 0.0, "Export/tourist refund: no VAT applied"
    elif location == "":
        return DEFAULT_TAX_RATE, f"Location not specified. Default VAT: {DEFAULT_TAX_RATE * 100:.0f}%"
    else:
        return DEFAULT_TAX_RATE, (
            f"Unknown location '{location}'. "
            f"Default Uganda VAT applied: {DEFAULT_TAX_RATE * 100:.0f}%"
        )


def calculate_final_price(subtotal, coupon_code, location):
    """Calculate final price with subtotal, discounts, and tax."""
    if subtotal < 0:
        return None, "Subtotal cannot be negative."

    volume_rate, volume_msg = get_volume_discount_rate(subtotal)
    volume_discount = subtotal * volume_rate

    coupon_discount, coupon_msg = apply_coupon(subtotal, coupon_code)

    total_discount = volume_discount + coupon_discount
    if total_discount > subtotal:
        total_discount = subtotal

    discounted_subtotal = subtotal - total_discount

    tax_rate, tax_msg = get_tax_rate(location)
    tax_amount = discounted_subtotal * tax_rate
    final_price = discounted_subtotal + tax_amount

    receipt = {
        "subtotal": subtotal,
        "volume_discount": volume_discount,
        "volume_msg": volume_msg,
        "coupon_discount": coupon_discount,
        "coupon_msg": coupon_msg,
        "total_discount": total_discount,
        "discounted_subtotal": discounted_subtotal,
        "tax_rate": tax_rate,
        "tax_msg": tax_msg,
        "tax_amount": tax_amount,
        "final_price": final_price,
    }
    return receipt, None


def print_receipt(receipt):
    """Display price breakdown."""
    print("\n" + "=" * 45)
    print("ORDER RECEIPT")
    print("=" * 45)
    print(f"Subtotal:              {format_ugx(receipt['subtotal'])}")
    print(f"  {receipt['volume_msg']}: -{format_ugx(receipt['volume_discount'])}")
    print(f"  {receipt['coupon_msg']}: -{format_ugx(receipt['coupon_discount'])}")
    print(f"After discounts:       {format_ugx(receipt['discounted_subtotal'])}")
    print(f"  {receipt['tax_msg']}")
    print(f"VAT amount:            {format_ugx(receipt['tax_amount'])}")
    print("-" * 45)
    print(f"FINAL PRICE:           {format_ugx(receipt['final_price'])}")
    print("=" * 45)


def prompt_price_calculation():
    """Collect inputs and run price calculation."""
    try:
        subtotal = float(input("\nEnter subtotal (USh): "))
    except ValueError:
        print("Invalid subtotal. Please enter a number.")
        return

    coupon_code = input("Enter coupon code (or press Enter to skip): ")
    location = input("Enter location (e.g. kampala, entebbe, jinja, mbarara): ")

    receipt, error = calculate_final_price(subtotal, coupon_code, location)
    if error:
        print(error)
    else:
        print_receipt(receipt)


def show_coupon_list():
    """Display available coupon codes."""
    print("\n--- AVAILABLE COUPONS ---")
    for code, details in COUPONS.items():
        if details["type"] == "percent":
            print(f"  {code}: {details['value']}% off (min {format_ugx(details['min_subtotal'])})")
        else:
            print(f"  {code}: {format_ugx(details['value'])} off (min {format_ugx(details['min_subtotal'])})")


def show_tax_rates():
    """Display VAT rates by location in Uganda."""
    print("\n--- VAT RATES BY LOCATION (UGANDA) ---")
    for location, rate in TAX_RATES.items():
        print(f"  {location.replace('_', ' ').title()}: {rate * 100:.0f}%")
    print(f"  Default / Unknown: {DEFAULT_TAX_RATE * 100:.0f}%")
    print("  Export / Tourist refund: 0%")


def show_user_list():
    """Display registered users (admin only)."""
    print("\n--- REGISTERED USERS ---")
    for username, user in USERS.items():
        print(f"  {username} | {user['name']} | Role: {user['role']}")


def admin_menu(user):
    """Admin has access to all features."""
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Calculate order price")
        print("2. View coupon codes")
        print("3. View tax rates")
        print("4. View all users")
        print("5. Process sale (cashier feature)")
        print("6. Shop as customer")
        print("7. Logout")

        choice = input("Your choice (1-7): ").strip()

        if choice == "1":
            prompt_price_calculation()
        elif choice == "2":
            show_coupon_list()
        elif choice == "3":
            show_tax_rates()
        elif choice == "4":
            show_user_list()
        elif choice == "5":
            cashier_process_sale(user)
        elif choice == "6":
            customer_shop(user)
        elif choice == "7":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")


def cashier_process_sale(user):
    """Cashier processes a sale for a customer."""
    print(f"\n--- CASHIER SALE (handled by {user['name']}) ---")
    customer_name = input("Customer name: ").strip() or "Walk-in customer"
    print(f"Processing order for: {customer_name}")
    prompt_price_calculation()
    print("Sale recorded. Thank you!")


def cashier_menu(user):
    """Cashier can process sales and calculate prices."""
    while True:
        print("\n--- CASHIER MENU ---")
        print("1. Process customer sale")
        print("2. Calculate order price")
        print("3. View coupon codes")
        print("4. View tax rates")
        print("5. Logout")

        choice = input("Your choice (1-5): ").strip()

        if choice == "1":
            cashier_process_sale(user)
        elif choice == "2":
            prompt_price_calculation()
        elif choice == "3":
            show_coupon_list()
        elif choice == "4":
            show_tax_rates()
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")


def customer_shop(user):
    """Customer shopping and checkout flow."""
    print(f"\n--- SHOPPING (Welcome, {user['name']}) ---")
    print("Sample products:")
    print(f"  1. Wireless Headphones - {format_ugx(295000)}")
    print(f"  2. USB-C Cable       - {format_ugx(48000)}")
    print(f"  3. Laptop Stand      - {format_ugx(165000)}")
    print("  4. Custom amount")

    choice = input("Select product (1-4): ").strip()
    if choice == "1":
        subtotal = 295000
    elif choice == "2":
        subtotal = 48000
    elif choice == "3":
        subtotal = 165000
    elif choice == "4":
        try:
            subtotal = float(input("Enter custom amount (USh): "))
        except ValueError:
            print("Invalid amount.")
            return
    else:
        print("Invalid product selection.")
        return

    coupon_code = input("Enter coupon code (or press Enter to skip): ")
    location = input("Enter your location for tax: ")

    receipt, error = calculate_final_price(subtotal, coupon_code, location)
    if error:
        print(error)
    else:
        print_receipt(receipt)
        confirm = input("\nConfirm purchase? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Order placed successfully! Thank you for shopping.")
        else:
            print("Order cancelled.")


def customer_menu(user):
    """Customers can shop and view coupons/tax info."""
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. Shop & checkout")
        print("2. Calculate order price")
        print("3. View coupon codes")
        print("4. View tax rates")
        print("5. Logout")

        choice = input("Your choice (1-5): ").strip()

        if choice == "1":
            customer_shop(user)
        elif choice == "2":
            prompt_price_calculation()
        elif choice == "3":
            show_coupon_list()
        elif choice == "4":
            show_tax_rates()
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")


def main():
    
    while True:
        user = login()

        if user:
            if user["role"] == "admin":
                admin_menu(user)
            elif user["role"] == "cashier":
                cashier_menu(user)
            elif user["role"] == "customer":
                customer_menu(user)
        else:
            retry = input("\nTry again? (yes/no): ").strip().lower()
            if retry != "yes":
                print("Goodbye!")
                break


if __name__ == "__main__":
    main()
