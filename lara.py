def calculate_discount(price,discount_percent):
    discount_amount = price * discount_percent
   

    if discount_percent  >= 20:
        # print("You get a discount of ",discount_amount)
        return discount_amount
    else:
        return price

        



print(calculate_discount(int(input("Enter the price: ")),float(input("Enter the discount percent: "))))
