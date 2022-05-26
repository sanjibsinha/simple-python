input_one = input('Enter mass of HydroCarbon in a floating point: ')
mass_of_hydrocarbon = float(input_one)
input_two = input('Enter the number of carbon atoms: ')
number_of_carbon_atoms = int(input_two)
input_three = input('Enter the number of hydrogen atoms: ')
number_of_hydrogen_atoms = int(input_three)
carbon_AMU = 12
hydrogen_AMU = 1
formula_weight_of_oneMole = (number_of_carbon_atoms * carbon_AMU) + (number_of_hydrogen_atoms * hydrogen_AMU)

avogadro_number = 6.02 * (10 ** 23)
molecules = (mass_of_hydrocarbon / formula_weight_of_oneMole) * avogadro_number

print(f'{mass_of_hydrocarbon} grams of hydrocarbon with {number_of_carbon_atoms} carbon atoms and {number_of_hydrogen_atoms} hydrogen atoms contain {molecules} molecules')

'''
Enter mass of HydroCarbon in a floating point: 16.0
Enter the number of carbon atoms: 1
Enter the number of hydrogen atoms: 4
16.0 grams of hydrocarbon with 1 carbon atoms and 4 hydrogen atoms contain 6.019999999999999e+23 molecules
'''