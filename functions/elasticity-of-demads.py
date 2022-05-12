# elastic

""" def find_increase_in_percentage_change_in_price(initial_price, percentage):
    increase_in_percentage_change = initial_price * (1 + percentage/100)
    return int(increase_in_percentage_change)

def find_decrease_in_percentage_change_in_price(initial_price, percentage):
    decrease_in_percentage_change = initial_price * (1 - percentage/100)
    return int(decrease_in_percentage_change)
def find_increase_in_percentage_change_in_quantity(initial_quantity, percentage):
    increase_in_percentage_change = initial_quantity * (1 + percentage/100)
    return int(increase_in_percentage_change)

def find_decrease_in_percentage_change_in_quantity(initial_quantity, percentage):
    decrease_in_percentage_change = initial_quantity * (1 - percentage/100)
    return int(decrease_in_percentage_change) """


def find_elasticity_of_demand(initial_price, percentage_change_in_price, 
                    initial_quantity, percentage_change_in_quantity):
    elasticity_of_demand = (initial_quantity - percentage_change_in_quantity / 
                            initial_quantity + percentage_change_in_quantity) * (
                                initial_price + percentage_change_in_price / 
                                initial_price - percentage_change_in_price
                            )
    
    return elasticity_of_demand

""" price_increase_percentage = find_increase_in_percentage_change_in_price(500, 10)
print(price_increase_percentage)
price_decrease_percentage = find_decrease_in_percentage_change_in_price(500, 10)
print(price_decrease_percentage)

quantity_increase_percentage = find_increase_in_percentage_change_in_quantity(60, 50)
print(quantity_increase_percentage)
quantity_decrease_percentage = find_decrease_in_percentage_change_in_quantity(60, 10)
print(quantity_decrease_percentage) """


elasticity_of_demand = find_elasticity_of_demand(500, 450, 
                                                 60, 90)

elasticity_of_demand_converted_to_integer = int(elasticity_of_demand)

if elasticity_of_demand_converted_to_integer > 1:
    print(f"Demand is Elastic and the elasticity coefficient is: {elasticity_of_demand_converted_to_integer}")
elif elasticity_of_demand_converted_to_integer == 1:
    print(f"Demand is Unitary Elastic and the elasticity coefficient is: {elasticity_of_demand_converted_to_integer}")
elif elasticity_of_demand_converted_to_integer < 1:
    print(f"Demand is Not Elastic and the elasticity coefficient is: {elasticity_of_demand_converted_to_integer}")
else:
    print(f"The value {elasticity_of_demand_converted_to_integer}")
