def calculate_total(price, quantity):
    total = price * quantity
    return total


price = 10
quantity = 5

subtotal = calculate_total(price, quantity)
discount = 60

final_price = subtotal - discount

print("Final price:", final_price)