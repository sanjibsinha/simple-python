def main():
    GetARangeOfNumber()
    
    
def GetARangeOfNumber():
    for index in IteratingStepByStep(1, 123, 7):
        print(index, end=' ')
    
    # 1 8 15 22 29 36 43 50 57 64 71 78 85 92 99 106 113 120
    
    
def IteratingStepByStep(start, stop, step):
    number = start
    while number <= stop:
        yield number
        number += step
        
if __name__ == "__main__": main()

# changed
