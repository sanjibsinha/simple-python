def find_elasticity_of_demand(initial_price, percentage_change_in_price, 
                    initial_quantity, percentage_change_in_quantity):
    elasticity_of_demand = (percentage_change_in_quantity 
                            / initial_quantity) * (initial_price 
                                                   / percentage_change_in_price)
    
    print(elasticity_of_demand)
    
find_elasticity_of_demand(500, 10, 30, 10)
find_elasticity_of_demand(500, 20, 30, 30)
find_elasticity_of_demand(500, 30, 30, 52)
find_elasticity_of_demand(500, 10, 56, 52)

'''
16.666666666666664
25.0
28.888888888888893
46.42857142857143
'''