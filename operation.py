import re
from read import read_furniture_data
from write import write_to_file
from invoice import generate_invoice  

def validate_name(name):
    """Ensuring that the name contains only alphabets and spaces, with no leading, trailing, or multiple consecutive spaces."""
    if re.match("^[A-Za-z]+(?: [A-Za-z]+)*$", name): 
    #It allows for more spaces in between the names and also ensure that it ends with valid characters
        return True
    return False

def find_items(furniture_list, item_id):
    # Function to find an item in the furniture list by its unique ID
    for item in furniture_list:  # Loop through each item
        if item['id'] == item_id:
            return item
    return None

def display_stock(furniture_list):
    # If the furniture list is empty, display a message
    if not furniture_list:
        print("No furniture items available in the inventory.")
        return

    # Print table header
    print("+----+-----------------------------------------+-------------------------+----------+------------+")
    print("| ID |  Manufacturer                           |          Name           | Quantity |   Price    |")
    print("+----+-----------------------------------------+-------------------------+----------+------------+")

    # Loop through each furniture item and print its details
    for furniture in furniture_list:
        # Format each row to align columns properly
        print(f"| {furniture['id']:<2} | {furniture['manufacturer']:<39} | {furniture['name']:<23} | {furniture['quantity']:<8} | ${furniture['price']:<9.2f} |")

    # Print table footer
    print("+----+-----------------------------------------+-------------------------+----------+------------+")

def purchase_furniture(file_name):
    # Function to manage furniture purchases from the manufacturers
    furniture_list = read_furniture_data(file_name)
    cart = []  # Create empty list

    while True:
        employee_name = input("Enter your Name: ").strip()
        if employee_name and validate_name(employee_name):
            break
        print("Error: Name cannot be empty and must contain only alphabets without any special characters or numbers.")

    while True:
        try:
            item_id = int(input("Enter furniture ID to purchase: "))
            quantity = int(input("Enter the amount of quantity to purchase: "))
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number.")
        except ValueError as e:
            print(f"Invalid input. {e}")
            continue

        item = find_items(furniture_list, item_id)

        if item:
            cart.append({'item': item, 'quantity': quantity})
            item['quantity'] += quantity 
            print(f"The {quantity} amount of item has been added from the {item['manufacturer']} to this Product ID {item_id}.")
        else:
            print(f"The entered {item_id} item ID is not found.")
        
        while True:
            try:
                continue_choice = input("Do you want to add more items to your Furniture store? (yes/no): ").strip().lower()
                if continue_choice not in ['yes', 'no']:
                    raise ValueError("Please enter 'yes' or 'no'.")
                break
            except ValueError as e:
                print(f"Invalid input. {e}")
        
        if continue_choice == 'no':
            break  # Exit the loop 

    if cart:
        while True:
            address = input("Enter the address for delivery: ").strip()
            if address:
                break
            print("Error: Address cannot be empty.")
            
        shipping_cost = 0
        
        if address.lower() != "itahari":
            while True:
                add_shipping = input("Do you want to add shipping cost to your receipt? (yes/no): ").strip().lower()
                if add_shipping in ['yes', 'no']:
                    break
                else:
                    print("Error: Please enter 'yes' or 'no'.")

            if add_shipping == 'yes':
                while True:
                    try:
                        shipping_cost = float(input("Enter the shipping cost: "))
                        if shipping_cost < 0:
                            raise ValueError("Shipping cost must be a non-negative number.")
                        break
                    except ValueError as e:
                        print(f"Invalid input. {e}")
        else:
            print("Free shipping within Itahari.")  # Free shipping within the Itahari Area
        
        vat_rate = 0.13
        vat_amount = 0
        total_amount = 0

        for entry_of_item in cart:     
            item = entry_of_item['item']   
            quantity = entry_of_item['quantity']
            total_amount += item['price'] * quantity
            vat_amount += (item['price'] * quantity) * vat_rate

        shipping_display = f"Shipping Cost: ${shipping_cost:.2f}" if address.lower() != "itahari" else "Free Shipping"

        generate_invoice(cart, employee_name, shipping_display, vat_amount, "Manufacture Order Bill", shipping_cost, address.lower() != "itahari", "purchase")

        write_to_file(file_name, furniture_list)
        print("Order has been placed successfully.")
    else:
        print("No products were chosen.")

def sell_furniture(file_name):
    # Function to sell the furniture items from the inventory
    furniture_list = read_furniture_data(file_name)
    cart = []  # Create empty list
    
    while True:
        customer_name = input("Enter customer name: ").strip()
        if customer_name and validate_name(customer_name):
            break
        print("Error: Name cannot be empty and must contain only alphabets without any special characters or numbers.")

    while True:
        try:
            item_id = int(input("Enter furniture ID to sell: "))
            quantity = int(input("Enter the amount of quantity to sell: "))
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number.")
        except ValueError as e:
            print(f"Invalid input. {e}")
            continue

        item = find_items(furniture_list, item_id)
        if item and item['quantity'] >= quantity:
            cart.append({'item': item, 'quantity': quantity})
            item['quantity'] -= quantity
            print(f"The {item['manufacturer']} has sold {quantity} amount of quantity to {customer_name}.")
        else:
            print(f"The entered ID {item_id} is not found or no more items left.")
        
        while True:
            try:
                continue_choice = input("Do you want to add more items? (yes/no): ").strip().lower()
                if continue_choice not in ['yes', 'no']:
                    raise ValueError("Please enter 'yes' or 'no'.")
                break
            except ValueError as e:
                print(f"Invalid input. {e}")

        if continue_choice == 'no':
            break  # Exit the loop 

    if cart:
        while True:
            address = input("Enter the address for delivery: ").strip()
            if address:
                break
            print("Error: Address cannot be empty.")
        
        shipping_cost = 0
        
        if address.lower() != "itahari":
            while True:
                add_shipping = input("Do you want to add shipping cost to the total amount? (yes/no): ").strip().lower()
                if add_shipping in ['yes', 'no']:
                    break
                else:
                    print("Error: Please enter 'yes' or 'no'.")

            if add_shipping == 'yes':
                while True:
                    try:
                        shipping_cost = float(input("Enter shipping cost: "))
                        if shipping_cost < 0:
                            raise ValueError("Shipping cost must be a non-negative number.")
                        break
                    except ValueError as e:
                        print(f"Invalid input. {e}")
        else:
            print("Free shipping within Itahari.")  # Free shipping within the Itahari Area
        
        vat_rate = 0.13
        vat_amount = 0
        total_amount = 0

        for entry_of_item in cart:
            item = entry_of_item['item']
            quantity = entry_of_item['quantity']
            total_amount += item['price'] * quantity
            vat_amount += (item['price'] * quantity) * vat_rate

        shipping_display = f"Shipping Cost: ${shipping_cost:.2f}" if address.lower() != "itahari" else "Free Shipping"

        generate_invoice(cart, customer_name, shipping_display, vat_amount, "Sales Bill", shipping_cost, address.lower() != "itahari", "Sale")

        write_to_file(file_name, furniture_list)
        print("Item has been sold successfully.")
    else:
        print("There were no products chosen for selling.")


def add_new_item(file_name):
    furniture_list = read_furniture_data(file_name)
    
    try:
        item_id = int(input("Enter the new furniture ID: "))
        manufacturer = input("Enter the manufacturer: ")
        name = input("Enter the name of the furniture: ")
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        price = float(input("Enter the price: "))
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        
    except ValueError as e:
        print(f"Invalid input. {e}")
        return
    
    new_item = {
        'id': item_id,
        'manufacturer': manufacturer,
        'name': name,
        'quantity': quantity,
        'price': price
    }
    
    furniture_list.append(new_item)
    write_to_file(file_name, furniture_list)
    print("New item has been added successfully.")
