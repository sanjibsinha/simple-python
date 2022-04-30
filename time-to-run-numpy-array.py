import time
import numpy as numpy
numpy.random.seed(0)
array_like_float = numpy.random.rand(5)
startTime = time.time()
time.sleep(1)
print("Time to wake up, ~1 seconds have passed!")
print(array_like_float)
endTime = time.time()
    
howMuchTimeForNumpy = endTime - startTime
print(f"It takes {howMuchTimeForNumpy} seconds.")

# It takes 3.003420829772949 seconds.