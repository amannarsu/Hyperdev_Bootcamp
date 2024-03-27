print("****This program determines the award a person competing in a triathlon will receive****")
print("The 3 events for the triathlon are swimming, cycling, and running")
usrSwim = input("Please enter how long the perticipent took for Swimming in Minutes: ")
usrSwim = int(usrSwim) #Cast the 1st number to integer
usrCyc = input("Please enter how long the perticipent took for Cycling in Minutes: ")
usrCyc = int(usrCyc) #Cast the 2nd number to integer
usrRun = input("Please enter how long the perticipent took for Running in Minutes: ")
usrRun = int(usrRun) #Cast the 3rd number to integer

totalTime = usrSwim + usrCyc + usrRun #total time it took for the user to complete the award
print("Total time it took:", totalTime) #Prints the total time it took for the Triathlon

#Below if statemant check which award the person get based on his score
# 0–100 minutes Provincial colours
#101–105 minutes Provincial half
#106–110 minutes Provincial scroll
#111+ minutes No award
if totalTime < 100:
    print("Award: Provincial colours")
elif (totalTime <= 105) and (totalTime > 100):
    print ("Award: Provincial half colours")
elif (totalTime <= 110) and (totalTime > 105):
    print ("Award: Provincial scroll")    
else:
    print ("No Award") 