#bill caluculator
print("------------Welcome to Store----------------------")
print("Happy to see you here")
print("Buy only what you need...smile always")
print("Please speak in polite language\n")

# Item price list
print("-------Item---------------------Price per unit")
print("-------Rice (1kg)-------------------₹50")
print("-------Sugar (1kg)------------------₹40")
print("-------Milk (1L)--------------------₹30")
print("-------Oil (1L)---------------------₹100\n")

# Prices dictionary
price_list = {
    "rice": 50,
    "sugar": 40,
    "milk": 30,
    "oil": 100
}

# Empty cart to store user items
cart = {}

# Ask how many items
n = int(input("How many different items do you want to buy? "))

for i in range(n):
    item = input(f"\nEnter item name #{i+1}: ").lower()
    if item in price_list:
        qty = int(input(f"Enter quantity of {item} (kg or L): "))
        cart[item] = qty
    else:
        print("Sorry, this item is not available in Varshi Store.")

# Final bill generation
subtotal = 0
print("\n-----------Final Bill-----------")

for item, qty in cart.items():
    unit_price = price_list[item]
    item_total = qty * unit_price
    subtotal += item_total
    print(f"{item.capitalize():<7}: {qty} x ₹{unit_price} = ₹{item_total}")

# GST and final amount
gst = subtotal * 0.05
final_amount = subtotal + gst

print("----------------------------------")
print(f"Subtotal           : ₹{subtotal}")
print(f"GST (5%)           : ₹{gst:.2f}")
print(f"Total Amount       : ₹{final_amount:.2f}")
print("----------------------------------")
print("Thanks for visiting Store")
