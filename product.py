from validator1 import *

mobile_list = []

while True:
    option = show_menu()
    if option == 1:
        product= get_data()


    elif option == 2:
        search_code=input("Enter the code you want to search for: ")
        result = find_by_code(mobile_list, search_code)
        if result:
            print("neme object is:",result)
            print(find_by_code(mobile_list, search_code))
        else:
            print("neme object not found.")


    elif option == 3:
        search_price = input("Enter the price of search item: ")
        result1 = find_by_price(mobile_list, search_price)
        if result1:
            print("neme object is:",result1)
            print(find_by_price(mobile_list, search_price))
        else:
            print("neme object not found.")



    elif option == 4:
        print("mobile list")
        show_list()

    elif option == 0:
        print("exit")
        break
    else:
        print("invalid input")
