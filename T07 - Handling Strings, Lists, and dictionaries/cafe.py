menu = ["Coffee", "Hot Chocolate", "Ice Cream","Cake"] #the Menu

stock_Dict = { "Coffee" : 200, #The stock for number of these items in stock
                "Hot Chocolate" : 181,
                "Ice Cream" : 40,
                "Cake" : 102
             }
price_Dict = { #the prices of the items, per item
                "Coffee" : 1.60,
                "Hot Chocolate" : 2.10,
                "Ice Cream" : 4.50,
                "Cake" : 6.00
             }

print("############### Stock Report ###############")
 
a = 0
total_stock = 0
while a < len(menu): #loop to calculate the stock for all items
    total_stock += (stock_Dict[menu[a]] * price_Dict[menu[a]]) #calculates the total stock and the total price
    print(f"--Current stock for {menu[a]} is {stock_Dict[menu[a]]} items worth £{(stock_Dict[menu[a]] * price_Dict[menu[a]])} ")
    a += 1

print(f">>Current Total stock available is worth £{total_stock}<<") #prints out the total stock worth in pounds
print("############### End of report ###############")