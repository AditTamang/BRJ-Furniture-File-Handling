import datetime

def generate_invoice(cart, person_name, shipping_display, vat_amount, invoice_title, shipping_cost, include_shipping,transaction_type):
    '''Creating a transaction invoice and saves it to a text file.'''
    
    #Generate a unique invoice number using the current moment time
    invoice_number = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    #It create a new receipt filename with the transactions type and invoice number
    receipt = f"{transaction_type}_invoice_{invoice_number}.txt"

    #File will open in write mode 'w'
    with open(receipt, 'w') as file:
        file.write("="*90 + "\n")
        file.write(f"       BRJ Furniture Store\n")
        file.write(f"Tarahara, Itahari, Sunsari\n")
        file.write(f"Phone no: 9807373362    Email: BRJfurniture@gmail.com\n")
        file.write("="*90 + "\n\n")
        
        #Receipt Title and entire details of the user's
        file.write(f"{invoice_title}\n")
        file.write(f"Name: {person_name}\n")
        file.write(f"Invoice Number: {invoice_number}\n")
        file.write(f"Transaction Type: {transaction_type}\n")
        file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("\n")
        file.write("|------------------------------------------------------------------------------------------|\n")
        file.write(f"{'ID':<8} {'Manufacturer':<30}  {'Name':<20}  {'Quantity':<10}  {'Price':<10}\n")
        file.write("|------------------------------------------------------------------------------------------|\n")

        total_amount = 0

        #Loop through each item in the cart and record its information on the invoice.
        for entry_of_item in cart:
            item = entry_of_item['item']
            quantity = entry_of_item['quantity']
            total_price = item['price'] * quantity
            total_amount += total_price
            file.write(f"{item['id']:<8}  {item['manufacturer']:<30}  {item['name']:<20}  {quantity:<10}  ${total_price:<10.2f}\n")

        file.write("\n")
        file.write("="*90 + "\n")
        file.write(f"Total Amount (excluding VAT) : ${total_amount:.2f}\n")
        file.write(f"VAT Amount: ${vat_amount:.2f}\n")

        #If shipping cost is included then show the shipping cost and add it to the total amount 
        if include_shipping:
            file.write(f"{shipping_display}\n")
            total_amount += shipping_cost

        #Calculate the total amount including with VAT
        total_with_vat = total_amount + vat_amount
        file.write(f"Total Amount (including VAT) : ${total_with_vat:.2f}\n")
        file.write("="*90 + "\n")
        
        file.write("\n")
        file.write("        Thank you for trusting us. Please visit us again\n")
        file.write("="*90 + "\n")
        file.write("            Certified Company, Nepal Government\n")
        file.write("="*90 + "\n")

    
    print(f" Thank you.!!! Your Invoice has been generated: {receipt}")
