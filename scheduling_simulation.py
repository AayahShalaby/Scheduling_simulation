#The purpose of this code is to simulate the order starter process in order to find an optimal time to complete 10
#orders before 9:30. This is done by initializing the start time at 8:30am, generating a random number of orders 
#in the range of 175-250, then simulating the times it takes to complete an order and icrementing it until 10 orders
#are reached. In order to find an optimal time to start, a minute is added to the starting time and the entire 
#process is repreated until 10 orders are completed or 10 orders are not completed by 9:30am. Therefore, the optimal
#time is the latest time allowable to start to ensure that 10 orders are completed.


from datetime import datetime, time, timedelta
import random

#start the start time to be 8:30 am 
start_time = time(8,30)

#set end time to be 9:30 am (time class)
end_time = time(9,30)

# Get the current date
curr_date = datetime.now().date()

# Combine the current date with the time value (datetime class)
real_end_time = datetime.combine(curr_date, end_time)

#get current date
current_date = datetime.now().date()

#get current date with start time which is 8:30am
current_datetime = datetime.combine(current_date, start_time)

#Initialyzing intervals to be one minute  
interval = timedelta(minutes=1)

#loop from 8:30am to 9:30 am
minimal_time = real_end_time - current_datetime
opt_time = current_datetime.time()
while current_datetime.time() <= end_time:
    print("NEW TEST TRIAL: ", current_datetime.time())
    s_time = current_datetime
    #generate a random number of orders form 175-250
    number_of_orders = random.randint(175,250)
    
    completed_orders = 0
    #loop for every order to find the time it takes to pack each order
    for i in range(1,number_of_orders +1):
        #time to pack a order ranges from 2-3 minutes 
        time_to_pack = random.uniform(2,3)
       
        s_time += timedelta(minutes = time_to_pack)
        completed_orders +=1
        print(completed_orders, "Orders completed. The time is now: ", s_time)
            
        #if the time is or past 9:30am but 10 have not been completed, exit the loop
        if (s_time > real_end_time and completed_orders<=10):
            print("reached max time. Orders completed: ",completed_orders)
            print("")
            break
        
        #if it is before 9:30 and 10 orders have completed, exit the loop
        elif (s_time < real_end_time and completed_orders >=10):
            print("10 orders completed in: ", s_time)
            print("time difference: ", real_end_time - s_time)
            print("")
            time_diff = real_end_time - s_time
            
            #see if the time difference is less than existing smallest time difference
            if time_diff < minimal_time:
                minimal_time = time_diff
                #opt_time = s_time
                opt_time = current_datetime.time()
            break    
            
    #go to next trial which is a minute later 
    current_datetime += interval

print("the optimal starting time is: ", opt_time)