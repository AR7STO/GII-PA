def calculate_cash_distribution(amount, denominations):
    """
    Simulates the distribution of cash in a simple ATM.

    Parameters:
    - amount (float): The total money to withdraw (can include cents).
    - denominations (list of float): The available bill/coin denominations in descending order.

    Returns:
    - dict: A dictionary showing the quantity of each denomination.
    """
    # Initialize a dictionary to store the results
    cash_distribution = {}

    # Convert the amount to cents to avoid floating-point issues
    amount_in_cents = round(amount * 100)

    # Convert denominations to cents
    denominations_in_cents = [round(denomination * 100) for denomination in denominations]

    # Loop through each denomination
    for denomination in denominations_in_cents:
        # Calculate how many of the current denomination are needed
        quantity = amount_in_cents // denomination
        if quantity > 0:  # Only include denominations used
            cash_distribution[denomination] = quantity
        # Reduce the remaining amount
        amount_in_cents %= denomination

    return cash_distribution

def display_cash_distribution(cash_distribution, denominations):
    """
    Displays the cash distribution in a detailed format.

    Parameters:
    - cash_distribution (dict): A dictionary with denominations as keys (in cents) and quantities as values.
    - denominations (list of float): The available bill/coin denominations in descending order.
    """
    # Convert denominations to cents for easy matching
    denominations_in_cents = [round(denomination * 100) for denomination in denominations]

    for denomination_in_cents in denominations_in_cents:
        if denomination_in_cents in cash_distribution:
            quantity = cash_distribution[denomination_in_cents]
            denomination = denomination_in_cents / 100  # Convert back to euros
            if denomination >= 5:
                unit = "bill"
            elif denomination >= 1:
                unit = "coin"
            else:
                unit = "cent coin"
            print(f"{quantity} {unit}(s) of {denomination:.2f}€")

# Main script
if __name__ == "__main__":
    # Denominations available in Spain
    available_denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]

    # Prompt user for the amount to withdraw
    while True:
        try:
            total_amount = float(input("Enter the amount you want to withdraw (e.g., 1234.67): "))
            if total_amount <= 0:
                print("The amount must be greater than 0. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 1234.67).")

    # Call the function
    result = calculate_cash_distribution(total_amount, available_denominations)

    # Display the result
    print("\nCash Distribution:")
    display_cash_distribution(result, available_denominations)
