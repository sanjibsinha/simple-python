# elasticity coefficient
changed_quantity = 50
initial_quantity = 30
initial_price = 12
changed_price = 8

def find_elasticity_of_demand(changed_quantity, initial_quantity, initial_price, changed_price):    
    
                             
                            
    
    print(((changed_quantity - initial_quantity) / (changed_quantity + initial_quantity)) / ((initial_price - changed_price) / (initial_price + changed_price))) 

print(((50 - 30)/(50+30))/((10-8)/(10+8)))
print(((changed_quantity - initial_quantity)/(changed_quantity+initial_quantity))/((initial_price-changed_price)/(initial_price+changed_price)))


find_elasticity_of_demand(50, 30, 12, 8)
""" 
elasticity_of_demand = find_elasticity_of_demand(500, 700, 
                                                 60, 70) """



""" if elasticity_of_demand > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {elasticity_of_demand}")
elif elasticity_of_demand == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {elasticity_of_demand}")
elif elasticity_of_demand < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {elasticity_of_demand}")
else:
    print(f"The value {elasticity_of_demand}")
 """