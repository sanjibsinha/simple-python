input_one = input('Enter the value of the line-slope in positive integer: ')
line_slope = int(input_one)

input_two = input('Enter the intercept of y-axis: ')
y_intercept = int(input_two)

input_three = input('Enter the value of x-coordinate: ')
x_coordinate = int(input_three)

y_coordinate = (line_slope * x_coordinate) + y_intercept

print(f'The y-coordinate is: {y_coordinate} when the ' 
      f'slope of the line is {line_slope}. '
      f'Intercept of y-axis is {y_intercept} ' 
      f'and X coordinate is: {x_coordinate}')

'''
The y-coordinate is: 23 when the slope of the line is 5. 
Intercept of y-axis is 3 and X coordinate is: 4
'''
# commiting to discrete