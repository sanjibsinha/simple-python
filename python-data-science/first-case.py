# elasticity coefficient

def find_elasticity_of_demand(changed_quantity, initial_quantity, initial_price, changed_price):
    elasticity_of_demand = ((changed_quantity - initial_quantity) / (changed_quantity + initial_quantity)) / (((initial_price - changed_price) / (initial_price + changed_price))                            )
    
    return elasticity_of_demand




""" elasticity_of_demand = find_elasticity_of_demand(500, 450, 
                                                 60, 90) """
elasticity_of_demand = find_elasticity_of_demand(50, 30, 10, 8)



if elasticity_of_demand > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {elasticity_of_demand}")
elif elasticity_of_demand == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {elasticity_of_demand}")
elif elasticity_of_demand < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {elasticity_of_demand}")
else:
    print(f"The value {elasticity_of_demand}")