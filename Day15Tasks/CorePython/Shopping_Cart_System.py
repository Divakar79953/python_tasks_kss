#Shopping Cart System

prices = {
    "apple": 30,
    "banana": 20,
    "milk": 40,
    "bread": 35
}

cart = []

try:
    n = int(input("How many items do you want to add? "))

    for i in range(n):
        item = input("Enter item name: ").lower()

        if item in prices:
            cart.append(item)
        else:
            print("Invalid item:", item)


    unique_cart = set(cart)

    
    total = 0

    for item in unique_cart:
        if item in prices:
            total += prices[item]

    print("Cart Items:", cart)
    print("Unique Items:", unique_cart)
    print("Total Cost:", total)

except ValueError:
    print("Invalid input! Please enter a number.")
