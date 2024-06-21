# Lesson 3: Assignments | Sets


# **Task 1: Flight Route Comparison** 
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out: 1. Destinations that both airlines fly to. 
# 2. Destinations unique to your airline. 
# 3. Whether there are any destinations that neither airline shares. 
# 
# **Example Code:**

# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}



def flight (destination):
    our_routes = {"LAX", "JFK", "CDG", "DXB"}
    competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
    for our_route in our_routes:
        if our_route in competitor_routes:
             print(f'{our_route} is the same destination .')
        
        elif our_route not in  competitor_routes:
            print (f"These routes {our_route} are unique to our airline. ")
        # elif our_route not in competitor_routes and competitor_routes not in our_route:
        #     print (f"These are the routes that we both do not share {our_route} and {competitor_routes}")
           
flight(None)

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_ids = set(customer_ids)

print(unique_ids)


