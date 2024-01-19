
# Collecting user input for flight city, number of nights and rental days 
while True: 
    City_menu = ["Nigeria", "Kenya", "Ghana"]
    city_flight = input("Please enter the city you will be flying to.  Nigeria, Kenya or Ghana:? ").capitalize()
    if city_flight not in City_menu:
        print(f"You have made an invalide selection. ")

    else:
        break
while True: 
    try: 
        num_nights = int(input("Please enter the number of nights you will be staying: "))
        rental_days = int(input("Please enter the number of days you will be renting a car: "))
        break

    except ValueError:
        print("You have made an invalid selection, please try aagain. ")

# Creating the hotel cost function with num_nights arguement 
def hotel_cost(num_nights): 
    price_per_night = 2500
    return num_nights * price_per_night

# Creating the plane cost function with city flight arguement    
def plane_cost(city_flight):
   
    if city_flight == "Nigeria":
        return 5000
    
    elif city_flight == "Kenya":
        return 5000
     
    else:
        city_flight == "Ghana"
        return 3500
    

# Creating the car rental function with rental days arguement 
def car_rental(rental_days): 
   daily_rate = 800
   return (rental_days * daily_rate)

# Creating the holiday cost function with hotel cost, plane cost and care rental functions as logic of the fucntion
def holiday_cost(num_nights, city_flight, rental_days):
   total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
   return total_cost

# Calculating the total holiday cost 
total = holiday_cost(num_nights, city_flight, rental_days)

# Printing out the details of the holiday    
print("\nDetails of your trip")
print(f""" 
      
Your travel city is : {city_flight}
The number of nights for your holiday is  : {num_nights}
The number of days for car rental is : {rental_days}
Your plane cost is :       ${plane_cost(city_flight)}
Your hotel cost is :       ${hotel_cost(num_nights)}
The car rental cost is :  ${car_rental(rental_days)}
Your total holiday cost is :  ${total}

""" ) 









