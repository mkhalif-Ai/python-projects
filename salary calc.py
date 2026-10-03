name = input("enter your name:")
hours = int(input("enter the hours work:"))
rate = float(input("enter the rates:"))
print(f"employee: {name}")
print(f"hours_worked: {hours}")
print(f"rate: ${rate}/hr")
gross_pay = rate*hours
print(f"gross_pay: {gross_pay}")
tax_percentage = 22/100
tax= gross_pay*tax_percentage
print(f"tax22%: {tax}")
net_pay = gross_pay - tax
print(f"net_pay: {net_pay}")