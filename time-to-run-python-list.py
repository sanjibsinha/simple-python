import time


a_python_list = [0.5488135,  0.71518937, 0.60276338, 0.54488318, 0.4236548]
startTime = time.time()
time.sleep(3)
print("Time to wake up, ~3 seconds have passed!")
print(a_python_list)
endTime = time.time()
    
howMuchTimeForPythonList = endTime - startTime
print(f"It takes {howMuchTimeForPythonList} seconds.")

# It takes 3.003795862197876 seconds.