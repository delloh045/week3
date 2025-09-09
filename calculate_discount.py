# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Only apply discount if 20% or higher
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price  # No discount applied


# --- Main Program ---
# Prompt user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Display result
print("Final price after discount:", final_price)
