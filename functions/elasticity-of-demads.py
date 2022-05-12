# elastic

def find_increase_in_percentage_change_in_price(initial_price, percentage):
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
    return int(decrease_in_percentage_change)


def find_elasticity_of_demand(initial_price, percentage_change_in_price, 
                    initial_quantity, percentage_change_in_quantity):
    elasticity_of_demand = (initial_quantity - percentage_change_in_quantity / 
                            initial_quantity + percentage_change_in_quantity) / (
                                initial_price - percentage_change_in_price / 
                                initial_price + percentage_change_in_price
                            )
    
    return elasticity_of_demand

price_increase_percentage = find_increase_in_percentage_change_in_price(500, 10)
print(price_increase_percentage)
price_decrease_percentage = find_decrease_in_percentage_change_in_price(500, 50)
print(price_decrease_percentage)

quantity_increase_percentage = find_increase_in_percentage_change_in_quantity(60, 2)
print(quantity_increase_percentage)
quantity_decrease_percentage = find_decrease_in_percentage_change_in_quantity(60, 10)
print(quantity_decrease_percentage)


elasticity_of_demand = find_elasticity_of_demand(500, price_decrease_percentage, 
                                                 60, quantity_increase_percentage)

if elasticity_of_demand > 1:
    print(f"Elastic {elasticity_of_demand}")
elif elasticity_of_demand == 1:
    print(f"Unitary Elastic {elasticity_of_demand}")
else:
    print(f"Not Elastic {elasticity_of_demand}")
