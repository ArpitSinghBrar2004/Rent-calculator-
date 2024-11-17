## Input we need from user 
# Total rent
# Total food ordered for snacking
# Electricity units spend
# charge per unit
# number of people liveing in room or flat 

##Output
# Total amount you have to pay 
rent=int(input("enter your hostel/flat/house rent = "))
food= int(input("enter the amount of food ordered ="))
electricity_spend=int(input("enter the amount of Electricity Spend ="))
Charge_per_unit=int(input("enter charge per unit ="))
persons = int(input("enter the persons liveing in room/flat ="))
total_bill= electricity_spend*Charge_per_unit

output=(food + rent + total_bill ) //persons
print ("Each person will pay =",output)