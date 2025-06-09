def write_to_file(file_name, furniture_list):
   # The updated furniture list is written by this function to the appropriate file.
    with open(file_name, 'w') as file:  #Loop through each items
        for item in furniture_list:
            file.write(f"{item['id']}, {item['manufacturer']}, {item['name']}, {item['quantity']}, ${item['price']:.2f}\n")



