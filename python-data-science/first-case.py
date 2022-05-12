# elasticity coefficient

def find_elasticity_of_demand(initial_price, changed_price, 
                    initial_quantity, changed_quantity):
    elasticity_of_demand = (initial_quantity - changed_quantity / 
                            initial_quantity + changed_quantity) * (
                                initial_price + changed_price / 
                                initial_price - changed_price
                            )
    
    return elasticity_of_demand




""" elasticity_of_demand = find_elasticity_of_demand(500, 450, 
                                                 60, 90) """
elasticity_of_demand = find_elasticity_of_demand(500, 700, 
                                                 60, 70)

elasticity_of_demand_converted_to_integer = int(elasticity_of_demand)

if elasticity_of_demand_converted_to_integer > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {elasticity_of_demand_converted_to_integer}")
elif elasticity_of_demand_converted_to_integer == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {elasticity_of_demand_converted_to_integer}")
elif elasticity_of_demand_converted_to_integer < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {elasticity_of_demand_converted_to_integer}")
else:
    print(f"The value {elasticity_of_demand_converted_to_integer}")
