import matplotlib.pyplot as plt

def find_line_of_slope(x1, y1, x2, y2):
    line_of_slope = (y2 - y1) /(x2 - x1)
    print(f'Line of slope is: {line_of_slope}')
    
find_line_of_slope(0, 3, 4, 23)

# Line of slope is: 5.0

plt.plot((0, 3), (4, 23))

plt.show()