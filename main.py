from read import read_furniture_data
from operation import purchase_furniture, sell_furniture, add_new_item, display_stock


print("\n")
print("""
      ************************************************************************************************************************************
#     *                                                BRJ Furniture Store                                                                 *
#     *                                                   Tarahara, Itahari, Sunsari                                                      *
#     ************************************************************************************************************************************
#     *                                                                                                                                    *
#     *                                   Welcome to the BRJ Furniture Store..!!!                                                                                   
#     *                                                                                                                                    *
#     *             We have a wide range of furniture items available, perfect for making your choice.                      *
#     *                                                                                                                                    *
#     *************************************************************************************************************************************
""")
print("\n")

def main(): #The main function that starts the program
    file_name = 'furniture.txt'
    while True: #Until the user decides to exit, the loop will keep displaying menu options.
        print("BRJ Furniture Management Store")
        print("-" * 60)  
        print("Option             |         Description")
        print("-" * 60)
        print("Click 1 and Enter: | Show all available items in the store")
        print("Click 2 and Enter: | Purchase from Manufacturer")
        print("Click 3 and Enter: | Sell items to Customer")
        print("Click 4 and Enter: | Add new items to the inventory")
        print("Click 5 and Enter: | Exit")
        print("-" * 60)
        print("\n")
        
        #Choosing options from the menu
        choice = input("Enter your choice (1-5):\n ")
        
        if choice == '1':
            furniture_list = read_furniture_data(file_name) # Read and show all the available items afrom the inventory
            display_stock(furniture_list)
        elif choice == '2':
            purchase_furniture(file_name)   #Purchasing items from the manufacturer
        elif choice == '3':
            sell_furniture(file_name)   #Selling items to the customer's
        elif choice == '4':
            add_new_item(file_name) #Adding new items in the inventory
        elif choice == '5':
            print("Thank you for visiting the shop..Hope to see you soon..!!!")
            break   #Closing the program and breaking the loop
        else:
            print("Error: Invalid number. Please try again with valid numbers.")

if __name__ == "__main__":
    main()  #Calling the main function


