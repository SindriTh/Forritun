print("Welcome to car rentals!")
continue_str = input("Would you like to continue (y/n)? ")

while(continue_str == "y"):
    customer_code = input("Customer code (b or d): ")
    number_of_days_int  = int(input("Number of days: "))
    odo_start_int  = int(input("Odometer reading at the start: "))
    odo_end_int  = int(input("Odometer reading at the end: "))
    
    miles_driven = odo_end_int - odo_start_int
    print("Miles driven: ",miles_driven)

    if(customer_code == "b"):
        amount_due = float(40 * number_of_days_int + (0.25 * miles_driven))
        
    elif(customer_code == "d"):
        if(miles_driven > 100*number_of_days_int): # deducts the included miles
            miles_driven -= 100 * number_of_days_int
        else:
            miles_driven = 0
        amount_due = float(60 * number_of_days_int + (0.25 * miles_driven))
        
    print("Amount due: ",round(amount_due,1))
    continue_str = input("Would you like to continue (y/n)? ")
