# elasticity coefficient

def find_elastic_demand(changed_quantity, initial_quantity, 
                              initial_price, changed_price):
    sub_q = changed_quantity - initial_quantity
    add_q = changed_quantity + initial_quantity
    sub_p = initial_price - changed_price
    add_p = initial_price + changed_price
    elastic_demand = (sub_q / add_q) / (sub_p / add_p)
    
    return elastic_demand

elastic_demand = find_elastic_demand(50, 30, 10, 8)
# Demand is Elastic and the elasticity coefficient is: 2.25
inelastic_demand = find_elastic_demand(50, 40, 12, 6)
# Demand is Not Elastic and the elasticity coefficient is: 0.3333333333333333
unitary_elastic = find_elastic_demand(40.4, 40, 10, 9.9)
rounding_unitary_elastic = round(unitary_elastic)
# Demand is Unitary Elastic and the elasticity coefficient is: 1

if elastic_demand > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {elastic_demand}")
elif elastic_demand == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {elastic_demand}")
elif elastic_demand < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {elastic_demand}")
else:
    print(f"The value {elastic_demand}")


if inelastic_demand > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {inelastic_demand}")
elif inelastic_demand == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {inelastic_demand}")
elif inelastic_demand < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {inelastic_demand}")
else:
    print(f"The value {inelastic_demand}")


if rounding_unitary_elastic > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {rounding_unitary_elastic}")
elif rounding_unitary_elastic == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {rounding_unitary_elastic}")
elif elastic_demand < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {rounding_unitary_elastic}")
else:
    print(f"The value {rounding_unitary_elastic}")