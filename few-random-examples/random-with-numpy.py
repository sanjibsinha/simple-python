import time
import numpy as numpy

# we can generate an array of float
numpy.random.seed(0)

array_like_float = numpy.random.rand(5)
startTime = time.time()
time.sleep(3)
print("Time to wake up, ~3 seconds have passed!")
print(array_like_float)
endTime = time.time()
    
howMuchTimeForNumpy = endTime - startTime
print(str(howMuchTimeForNumpy) + " sec")

# [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]

a_python_list = [0.5488135,  0.71518937, 0.60276338, 0.54488318, 0.4236548]
startTime = time.time()
time.sleep(3)
print("Time to wake up, ~3 seconds have passed!")
print(a_python_list)
endTime = time.time()
    
howMuchTimeForPythonList = endTime - startTime
print(str(howMuchTimeForPythonList) + " sec")
# [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]

the_difference = howMuchTimeForNumpy - howMuchTimeForPythonList
print(f"The difference is : {the_difference}")

# we can generate a two-dimensional array
numpy.random.seed(0)

two_dimensional_array = numpy.random.rand(3, 5)
print(two_dimensional_array)


