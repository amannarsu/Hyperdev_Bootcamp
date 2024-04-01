#Informs the user about the holiday destinations
print("This program lets you book Holidays for 3 destinations: <<1. India ,2. Canada, 3. USA>>") 


city_flight = input("Please enter your holiday destination: ")# user input for destination
num_Nights = int(input("Please enter how many days you would like to stay for: "))# user input for hotel
rental_days = int(input("Please ented how many days you would need a car rental: "))# user input for car


def hotel_cost(a):#defined function for cost of hotel in total
    total_Hotel_cost = a * 102
    return total_Hotel_cost

def plane_cost(a):#defined function to assign flight cost based on selected location
   if a == "India" or a == "india"or a == 1: 
       flight_Cost =  750
       return flight_Cost
   elif a == "Canada" or a == "canada"or a == 2:
       flight_Cost = 1280
       return flight_Cost
   elif a == "USA" or a == "usa"or a == 3:
       flight_Cost = 950
       return flight_Cost
   else:
      print ("Sorry! you have typed in something incorrect or the country is not available in the list of destinations")

def car_rental(a):#defined function for cost of total car rental
    days_Rent = a * 45
    return days_Rent

def holiday_cost(num1, num2, num3 ):#defined function to calculate what user has to pay for the holiday package
                 total =num1 + num2 + num3
                 return total

#Outputs details to the user in a readable manner
print (f"Total cost of the holiday to {city_flight} for {num_Nights} nights with car rental of {rental_days} days is: £{holiday_cost(hotel_cost(num_Nights),plane_cost(city_flight),car_rental(rental_days)) }")


"""
Example of Results:
# For USA 4 days hotel and 3 days car rental: "Total cost of the holiday to USA for 4 nights with car rental of 3 days is: £1493"
# For US 3 days hotel and 3 days car rental: "TypeError: unsupported operand type(s) for +: 'int' and 'NoneType' "
# For India 7 days hotel and 6 days car rental: "Total cost of the holiday to india for 7 nights with car rental of 6 days is: £1734"
# For canada 21 days hotel and 20 days car rental: "Total cost of the holiday to canada for 21 nights with car rental of 20 days is: £4322"

"""