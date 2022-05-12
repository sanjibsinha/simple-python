# elasticity coefficient

def find_elasticity_of_demand(changed_quantity, initial_quantity, 
                              initial_price, changed_price):
    sub_q = changed_quantity - initial_quantity
    add_q = changed_quantity + initial_quantity
    sub_p = initial_price - changed_price
    add_p = initial_price + changed_price
    elasticity_of_demand = (sub_q / add_q) / (sub_p / add_p)
    
    return elasticity_of_demand

# elasticity_of_demand = find_elasticity_of_demand(50, 30, 10, 8)
# Demand is Elastic and the elasticity coefficient is: 2.25
elasticity_of_demand = find_elasticity_of_demand(50, 40, 12, 6)
# Demand is Not Elastic and the elasticity coefficient is: 0.3333333333333333

if elasticity_of_demand > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {elasticity_of_demand}")
elif elasticity_of_demand == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {elasticity_of_demand}")
elif elasticity_of_demand < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {elasticity_of_demand}")
else:
    print(f"The value {elasticity_of_demand}")