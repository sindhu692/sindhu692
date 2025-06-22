#>>>>>>>>>>>>>TEMP CONVERTOR<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print("Welcome to temp convertor")
n = input("How r u my dear: ")
if n == "good":
    print("That's great to hear you")
elif n == "bad":
    print("I will pray for you a great time")
else:
    print("Thanks for replying")

print("Have a great day")
print("Do you want to convert")
print("1) Celsius to Fahrenheit")
print("2) Fahrenheit to Celsius")

while True:
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        user = float(input("Enter your temp: "))
        f = (user * 9 / 5) + 32
        print(f"Converted to Fahrenheit: {f:.2f}°F")
        print("Thank you")

    elif choice == 2:
        user = float(input("Enter your temp: "))
        c = (user - 32) * 5 / 9
        print(f"Converted to Celsius: {c:.2f}°C")
        print("Thank you")

    else:
        print("Invalid input.. please try again")  # No need for symbols check separately

    want_to_continue = input("Do you want to convert again? (yes/no): ")
    if want_to_continue.lower() != "yes":
        break
