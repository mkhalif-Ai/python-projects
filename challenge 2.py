price = 10
quantity = int(input("how many do you want?"))
tax_percentage = 0.25
subtotal = price*quantity
tax = subtotal * tax_percentage
total = subtotal+tax
print(f"subtotal:{subtotal}")
print(f"tax is:{tax}")
print(f"total is:{total}")