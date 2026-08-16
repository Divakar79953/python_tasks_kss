# Store
products={"Pen":10,"Notebook":35,"Pencil":5}
cart=[]
categories={"Stationery","Books","Writing"}
pen_details=("Pen",10,"Stationery")
def display_products():
    print("Avaliable products:")

    for product,price in products.items():
        print(product,":",price)

def add_to_cart():
    product_name=input("Enter the product name:")

    try:

       quantity=int(input("Enter quantity:"))
    except ValueError:
        print("Invalid qunatity please enter a number:")
        return

    cart.append((product_name,quantity))

def calculate_total(cart,index=0):
    if index==len(cart):
        return 0

    product_name,quantity=cart[index]
    price=products[product_name]

    total=(price*quantity)+calculate_total(cart,index+1)

    return total

while True:
    print("1.Display Products")
    print("2.Add item to cart")
    print("3.View total bill")
    print("4.Exit")

    choice=int(input("Enter choice:"))

    if choice==1:
          display_products()
    elif choice==2:
        add_to_cart()
    elif choice==3:
        total=calculate_total(cart)
        print("Total Bill:",total)

    elif choice==4:
        break
    else:
        print("Invalid Choice")
        

