# Cafe Management Program

# Creating the menu
menu = {
    "Espresso": 79,
    "Latte": 59,
    "Cappuccino": 99,
    "MacAlooTiki Burger":49,
    "VegSurprise Burger":79,
    "Mac Cheese Burger":69,
    "Chicken Burger":69,
    "Hardcore Hazzlenut cone":49,
    "Creampie Vanilla cone":39,
    "Racist Chocolate":29,
    "Small fries":39,
    "Medium fries":59,
    "Large fries":69,
    "Cheesy fries":79,
}
menu1 = {
    "1": 79,
    "2": 59,
    "3": 99,
    "4":49,
    "5":79,
    "6":69,
    "7":69,
    "8":49,
    "9":39,
    "10":29,
    "11":39,
    "12":59,
    "13":69,
    "14":79,
}
#crew
crew="Manoj Bajpai"
crew_id=9075663
# Taking customer order
def take_order():
    order = {}
    while True:
        item = input("Enter the item you want to order (or 'done' to finish): ")
        if item == "done":
            break
        if item not in menu1:
            print("Sorry, we don't have that item.")
            continue
        quantity = int(input("Enter the quantity: "))
        if quantity<0:
            print("Please order in postive number")
            quantity = int(input("Enter the quantity: "))
        b=quantity
        order[item] = quantity
    return order  
        

# Calculating the bill
def calculate_bill(order):
    total = 0
    for item, quantity in order.items():
        total += menu1[item] * quantity
    return total

# User interface
def user_interface():
    print("____________________________________________________________________________________")
    print("\t \t \t \t Welcome to the Cafe Management Program!")
    while True:
        print("____________________________________________________________________________________")
        print("1.Items Available For Customer")
        print("2. Take Order")
        print("3. Calculate Bill")
        print("4. Show Order")
        print("5. Exit")
        print("6.Data")
        choice = input("Enter your choice: ")
        print("__________________________________________________________________________________")
        if choice == "2":
            order = take_order()
            print("\t--------Order taken successfully!---------")
        elif choice == "3":
            order_type=input("Enter  Order type(Dine-in,Take-away,Delivery)")
            cust_name=input("Enter Customer Name")
            cust_no=int(input("Enter Customer Contact Number"))
            pay=input("Mode of Paymet[UPI/Card/Cash]")
            order_number=int(input("Enter Order Number"))
            if pay=='cash':
                x=int(input("Enter Cash Received"))
                y=int(input("Enter Change given"))
                bill = calculate_bill(order)
                data={}
                data['Customer Name']=cust_name
                data['Customer Contact Number']=cust_no
                data['order']=order.items()
                data['order_type']=order_type
                data['change given']=y
                print("*************YOUR ORDER NUMBER IS-",order_number,"***************")
                print("\t             Bakingum Cafe")
                print("\t             Laxmi Nagar,Delhi-92")
                print( "                     Crew id-",         crew_id,         crew)
                print("___________________________________________________________________________________")
                print("Qty  Ordered Items      Items Price")        
                for key,value in order.items():
                    a=(f"{key}")
                for key,value in order.items():
                    b=(f"{value}")
                    c=menu[a]
                print(f"{value}          {key}","\t ₹",menu[a],"*",b)
                print("\t\t\t",f"Total bill: ₹{bill}")
                print("----Change given-----₹",y)
                print("Thank you",cust_name,"for choosing Bakingum Cafe ! We hope you enjoyed your experience")
            else:
                
                bill = calculate_bill(order)
                data={}
                data['Customer Name']=cust_name
                data['Customer Contact Number']=cust_no
                data['order']=order.items()
                data['order_type']=order_type
                print("*************YOUR ORDER NUMBER IS-",order_number,"***************")
                print("\t             Bakingum Cafe")
                print("\t             Laxmi Nagar,Delhi-92")
                print( "                     Crew id-",         crew_id,"Crew------",crew,"------")
                print("___________________________________________________________________________________")
                print("Qty  Ordered Items      Items Price")        
                for key,value in order.items():
                    a=(f"{key}")
                    b=(f"{value}")
                    
                    c=menu[a]
                    print(f"{value}          {key}","\t ₹",  menu[a],"*",b)
                print("\t\t\t",f"Total bill: ₹{bill}")
                print("Thank you",cust_name,"for choosing Bakingum Cafe ! We hope you enjoyed your experience")    

        elif choice == "5":
                print("Thank you for using the Cafe Management Program!")
                break
        elif choice == "4":
            for key,value in order.items():
                  print(f"{key}  * {value}")      
        elif choice == "1":       
            print("\nMenu:")
            print("------------------------------------------------------------------------------------------------------------------------------------------")
            
            print("************************************************************************************")
            print("------------------------------------------------------------------------------------------------------------------------------------------")     
            for item, price in menu.items():
                print(f"{item}: ₹{price}")
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            print("**********************************************************************************")
            print("----------------------------------------------------------------------------------------------------------------------------------------")
        elif choice=="6":
            print("Data stored in the dictionary:")
            for key, value in data.items():
                print(data)
                break
        else:
            print("------------------------------------------------------------------------------------------------------------------------------------------")
            print("Invalid choice. Please try again.")
            print("-----------------------------------------------------------------------------------------------------------------------------------------")

# Running the program
if __name__ == "__main__":
    user_interface()
