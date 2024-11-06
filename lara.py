def calculate_discount(price,discount_percent):
    discount_amount = price * discount_percent
    return discount_amount

print(calculate_discount(int(input("Enter the price: ")),float(input("Enter the discount percent: "))))