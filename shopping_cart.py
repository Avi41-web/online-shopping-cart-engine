
# Online Shopping Cart Engine
# Python Project

# Store product details
products = {
    1: {"name": "Shirt", "price": 500},
    2: {"name": "Shoes", "price": 1500},
    3: {"name": "Watch", "price": 1000},
    4: {"name": "Headphones", "price": 800},
    5: {"name": "Backpack", "price": 1200}
}

# Store items selected by the customer
cart = {}


# Display all available products
def display_products():
    print("\n------ AVAILABLE PRODUCTS ------")

    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} - "
            f"Rs.{product['price']}"
        )


# Add a product to the cart
def add_to_cart():
    display_products()

    try:
        product_id = int(input("\nEnter product number: "))

        if product_id not in products:
            print("Invalid product number!")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        # Add quantity if product is already in cart
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        print("Product added to cart successfully!")

    except ValueError:
        print("Please enter valid numbers!")


# Calculate the subtotal
def calculate_subtotal():
    subtotal = 0

    for product_id, quantity in cart.items():
        price = products[product_id]["price"]
        subtotal += price * quantity

    return subtotal


# Display cart items
def view_cart():
    print("\n------ YOUR SHOPPING CART ------")

    if not cart:
        print("Your cart is empty.")
        return

    for product_id, quantity in cart.items():
        product = products[product_id]
        item_total = product["price"] * quantity

        print(
            f"{product['name']} | "
            f"Quantity: {quantity} | "
            f"Price: Rs.{item_total}"
        )

    print(f"Subtotal: Rs.{calculate_subtotal()}")


# Remove a product from the cart
def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    try:
        product_id = int(
            input("\nEnter product number to remove: ")
        )

        if product_id in cart:
            del cart[product_id]
            print("Product removed from cart!")
        else:
            print("That product is not in your cart.")

    except ValueError:
        print("Please enter a valid product number!")


# Generate the final bill
def checkout():
    if not cart:
        print("\nYour cart is empty. Add products first.")
        return

    view_cart()

    subtotal = calculate_subtotal()

    # Apply a 10% discount for bills of Rs.2000 or more
    if subtotal >= 2000:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_total = subtotal - discount

    print("\n========== FINAL BILL ==========")
    print(f"Subtotal:    Rs.{subtotal:.2f}")
    print(f"Discount:    Rs.{discount:.2f}")
    print(f"Final Total: Rs.{final_total:.2f}")
    print("Thank you for shopping!")
    print("================================")


# Main program
while True:
    print("\n====== ONLINE SHOPPING CART ======")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Remove Product from Cart")
    print("5. Checkout and Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        display_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        checkout()
        print("Program closed.")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
