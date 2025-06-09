def read_furniture_data(filename):
     # It will read the furniture_list 
    furniture_list = [] # Creating List to store data
    try:
        # File will open in read mode 'r'
        with open(filename, 'r') as file:
            for line in file:   #Loop through each line
                if line.strip():
                    elements = line.strip().split(', ')
                    
                    #Creating a dictionary for each furniture items
                    furniture = {
                    'id': int(elements[0]),
                    'manufacturer': elements[1],
                    'name': elements[2],
                    'quantity': int(elements[3]),
                    'price': float(elements[4].replace('$', ''))
                    }
                    furniture_list.append(furniture)    #Adding the dictionary items to the List
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
    return furniture_list   
