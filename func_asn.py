#function that calculates final price after discount 
def calculate_discount(price, discount_percent):
  discount = discount_percent / 100  # Convert percentage to decimal

  if discount >= 0.2:  # Apply discount only if 20% or higher
    final_price = price * (1 - discount)
  else:
    final_price = price

  return final_price

# Example
original_price = 100
discount = 25
final_price = calculate_discount(original_price, discount)
print(f"Original price: ${original_price:.2f}")
print(f"Discount: {discount}%")
print(f"Final price after discount: ${final_price:.2f}")
