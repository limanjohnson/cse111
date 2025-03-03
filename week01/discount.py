from datetime import datetime
import math
import os

current_date_time = datetime.now()

day_of_the_week = current_date_time.weekday()

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

os.system('clear')
subtotal = int(input("Please enter the subtotal: "))
sales_tax_rate = .06

total = 0

if days == 1 or days == 2:
    if subtotal >= 50:
        customer_discount = round(subtotal * .1, 2) 
        sales_tax = round((subtotal - customer_discount) * sales_tax_rate, 2)
        total = subtotal - customer_discount + sales_tax
        print(f"Customer Discount: ${customer_discount}")
        print(f"Sales Tax: ${sales_tax}")
    else:
        difference_to_receive_discount = round(50 - subtotal, 2)
        print(f"Spend ${difference_to_receive_discount} in order to receive a 10% discount")
        sales_tax = round(subtotal * sales_tax_rate, 2)
        total = round(subtotal + sales_tax, 2)
        print(f"Sales Tax: ${sales_tax}")

else:
    sales_tax = round(subtotal * sales_tax_rate, 2)
    total = round(subtotal + sales_tax, 2)
    print(f"Sales Tax: ${sales_tax}")


print(f"Total: ${total}")